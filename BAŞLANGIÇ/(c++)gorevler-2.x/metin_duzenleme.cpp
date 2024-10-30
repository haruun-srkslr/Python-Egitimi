#include<iostream>
#include<string>
#include<fstream>
#include<sstream>
#include<vector>
#include<algorithm>
using namespace std;

vector<string> dosyaOkuma()
{
    string filename,satirlar,kelime;
    vector<string> kelimeler;
    cin>>filename;
    ifstream file(filename);
    
    if (file.is_open())
    {
        while(getline(file,satirlar))
        {
        istringstream iss(satirlar);
        while(iss>>kelime)
        {
        string temizKelime;
        for(char c : kelime)
        {
            if (isalpha(c)||isdigit(c))
            {
                temizKelime+=tolower(c);
            }
        }
        if(!temizKelime.empty()){
            kelimeler.push_back(temizKelime);
        }
        }    
        }

    return kelimeler;


    }
    else
    {
        return kelimeler;
    } 

}
vector<string> kelime_bulma(vector<string> kelimes)
{
    string degisen;
    vector<string>yeni_icerik;
    cout<<"hangi kelimeyi degistirmek istersiniz : ";
    cin>>degisen;
    int count=0;
    for(auto c:degisen)
    {
        c=tolower(c);
    }
    for(auto kelime: kelimes)
    {
        if(kelime==degisen)
        count+=1;

    }
don1:
    cout<<degisen<<"kelimesi \" "<<count<<"\""<<"adet bulundu degistirmek ister misiniz(E/H)"<<endl;
    char choice;
    cin>>choice;
    choice=tolower(choice);
    if(choice == 'e')
    {
        string yeni_kelime;
        cout<<"yeni kelime giriniz : ";
        cin>>yeni_kelime;
        for(size_t i=0;i<kelimes.size();i++)
        {
            if(kelimes[i]==degisen)
            {
                yeni_icerik.push_back(yeni_kelime);

            }
            else
            {
                yeni_icerik.push_back(kelimes[i]);
            }

        
        }
    return yeni_icerik;
        
        

    }
    else if(choice=='h')
    {
        cout<<"kelime degismeyecek"<<endl;

    }
    else
    {
        cout<<"hatali secim yaptiniz ! "<<endl;
        goto don1;
    }
   
}

void dosya_yaz(vector<string> yeni_icerik)
{
    ofstream file("duzenlenmis.txt", ios::app);
    if(file.is_open())
    {
        for(auto c:yeni_icerik)
        {
            file<<c<<" ";
        }
        file<<"---------------------"<<endl;

    }






}








int main()
{
vector<string> kelimeler;
vector<string> yeni;
kelimeler=dosyaOkuma();
yeni = kelime_bulma(kelimeler);
dosya_yaz(yeni);


return 0;

}