#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<algorithm>


using namespace std;




vector<string> dosyaOkuma()
{
    vector<string> kodlar;
    string filename,satirlar;
    cout<<"dosya adi giriniz";
    cin>>filename;
    ifstream file(filename);
    if(file.is_open())
    {
        while (getline(file,satirlar))
        {
            kodlar.push_back(satirlar);

        }
        

    }
    file.close();
    return kodlar;
}

string Isbn13(string& kod)
{

    int toplam=0;
    for(int i=0;i<kod.length();i++)
    {
        if(i%2==1)
        {
            toplam+=(kod[i]-'0')*3;
        }
        else
        {
            toplam+=(kod[i]-'0');
        }
    }
    if(toplam % 10 == 0)
    {
        return "gecerli ISBN-13 kodu";
    }
    else
    {
        return "gecersiz ISBN-13 kodu";
    }



}




string Isbn10(string& kod)
{
    int a,toplam=0;
    int kontrolDegeri;
    for(int i=0;i<kod.length()-1;i++)
    {
        if(isdigit(kod[i]))
        {
        int sonuc=0;
        int k1=kod[i]-'0';
        sonuc=(i+1)*k1;   
        toplam+=sonuc;
        }
        else
        {
            return "gecersiz ISBN";
        }

        char kontrol=kod[9];
        
        if (kontrol=='X'||kontrol =='x')
        {
            kontrolDegeri=10;
        }
        else if(isdigit(kontrol))
        {
            kontrolDegeri=kontrol-'0';

        }
        else
        {
            return "gecersiz ISBN";
        }
        

    }
    if(toplam%11==kontrolDegeri)
    {
        return "gecerli ISBN-10 KODU";
    }
    else
    {
        return "gecersiz ISBN-10 KODU";
    }

}



string harfKont(string& kod)       
{
    try{
        
        kod.erase(remove(kod.begin(), kod.end(), '-'), kod.end());
        
        if(kod.length()==10)
        {
            return Isbn10(kod);
        }
        else if(kod.length()==13)
        {
            return Isbn13(kod);
        }
        else{
            return "hatali giris var !";
        }
    }
    catch(const exception& e)
    {
        cerr<<"hata olustu"<<e.what() <<endl;
        return "hata olustu";
    }

}

void dosya_yazma(const vector<pair<string,string>> sonuclar)
{
    ofstream file("ISBN.txt", ios::app);
    if(file.is_open())
    {
       for(auto sonucs : sonuclar)
        {
        file<<sonucs.first<<"-->"<<sonucs.second<<endl;
        
        } 



    }
file.close();


}








int main()
{
    vector<string> kodlar=dosyaOkuma();
    vector<pair<string,string>>sonuclar;
    string kod;
    for(string& kod:kodlar)
    {

        string sonuc=harfKont(kod);
        sonuclar.push_back(make_pair(kod,sonuc));

    }
    dosya_yazma(sonuclar);






}