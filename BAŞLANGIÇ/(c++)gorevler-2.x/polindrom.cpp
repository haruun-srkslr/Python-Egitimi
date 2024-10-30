#include<iostream>
#include<string>
#include<fstream>
#include<sstream>
#include<vector>

using namespace std;

string dosya_okuma(string filename)
{
    string satirlar,kelimeler;
    ifstream file(filename);
    if(file.is_open())
    {
        while(getline(file,satirlar))
        {
            for(char a:satirlar)
            {
                kelimeler+=tolower(a);
            }
        }
    return kelimeler;
    
    }

}
vector<string> metniTerscevir(string kelimeler)
{
    string temizKelime1;
    vector<string> vect;
    vector<string> vect2;
    vector<string> poli;
    for(char b:kelimeler)
    {
        if(isalpha(b)||isspace(b)||isdigit(b))  
        {
            temizKelime1+=b;
        }
    }
    istringstream iss2(temizKelime1);
    string duzkelime;
    while (iss2>>duzkelime)
    {
        vect2.push_back(duzkelime);
    }
    
    // for (auto d:vect2)
    // {
    //     cout<<d<<endl;
    // }
    
    
    
    
    kelimeler=string(kelimeler.rbegin(),kelimeler.rend());
    string temizKelime;
    for(char a:kelimeler)
    {
        if(isalpha(a)||isspace(a)||isdigit(a))  
        {
            temizKelime+=a;
        }
    }
    istringstream iss(temizKelime);
    string ters;
    while (iss>>ters)
    {
        vect.push_back(ters);
    }
    
    
    // for (auto c:vect)
    // {
    //     cout<<c<<endl;
    // }

    for(size_t i=0;i<vect2.size();i++)
    {
        for(size_t j=0;j<vect.size();j++)
        if(vect[j]==vect2[i])
        {
            poli.push_back(vect[j]);
            cout<<vect[j]<<endl;;

        }
    }

    ofstream file("report.txt",ios::app);
    if(file.is_open())
    {
        file<<kelimeler<<endl;
        file<<"polindrom kelimeler : ";
        for(auto x:poli)
        {
            file<<x<<" ";
        }
        file<<endl;
        file<<"---------------------------------------------------------"<<endl;

    }








}











int main()
{
    string filename;
    cout<<"dosya adi giriniz : ";
    cin>>filename;
    string metin=dosya_okuma(filename);
    metniTerscevir(metin);

}