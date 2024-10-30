#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

vector<string> int_to_sayi(vector<int>& sayilar)
{
    vector<string> sonuclar;
    for(auto sayi:sayilar)
    {
    
    vector<pair<int, string>> roman_numerals = {
            {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
            {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"},
            {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
        };
    if (sayi<0 ||sayi>4000)
    {
        cout<<"lütfen 0 ile 4000 arasinda sayilari giriniz"<<endl;
        sonuclar.push_back("hatali sayi");
    }
    string roman_num="";
    while (sayi>0)
    {
        for(const auto& pair : roman_numerals)
        {
            int value=pair.first;
            const string& romans=pair.second;
            int count=sayi/value;
            roman_num += string(count, romans[0]);
            sayi-=count*value;
        }
        sonuclar.push_back(roman_num); 
    }
    }
    return sonuclar;
}

vector<int> dosya_okuma()
{
    vector<int> sayilar;
    string satirlar,filename;
    cout<<"lütfen dosya adini giriniz : ";
    cin>>filename;
    ifstream file(filename);
    if (file.is_open())
    {
        while(getline(file,satirlar)){
            int satir=stoi(satirlar);
            sayilar.push_back(satir);
        }

    }
    return sayilar;


}

void dosya_yazma(const vector<string>& sonuclar,vector<int>& inputlar)
{  
    ofstream file("output.txt");
    if(file.is_open())
    {
        for(size_t i=0;i<sonuclar.size();i++)
        {
            file<<sonuclar[i]<<"---->"<<inputlar[i]<<endl;
            file<<"-------------------------------------"<<endl;

        }
    }





}









int main()
{
    vector<int> sayilar;
    vector<string> sonuclar;
    sayilar=dosya_okuma();
    sonuclar=int_to_sayi(sayilar);
    dosya_yazma(sonuclar,sayilar);



    
}