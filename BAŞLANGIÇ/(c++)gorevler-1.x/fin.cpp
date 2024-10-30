#include<iostream>
#include<string>
using namespace std;
int max_size=100;
string fibonacci();
string fibonacc_coz();
int main()
{
    while (true) {
        cout << "\n1. SIFRELE\n";
        cout << "2. COZUMLE\n";
        cout << "3. CIKIS\n";
        cout << "---LUTFEN SECIM YAPINIZ (1-3)---\n";
        string secim;
        cin>>secim;
        if (secim=="1")
        {
            string sifrelenmis=fibonacci();
            cout<<"sifrelenmis metin : "<<sifrelenmis<<endl;
        }
        else if(secim=="2")
        {
            string cozulmus=fibonacc_coz();
            cout<<"cozulmus metin : "<<cozulmus<<endl;

        }
        else if(secim=="3")
        {
            cout<<"cikis yapiliyor ..."<<endl;
            break;
        }
        else
        {
            cout<<"hatali secim yaptiniz !";
        }
        
        
        }
    
    return 0;






}

string fibonacci()
{
    string metin,sifre;

    cout<<"sifrelemek istediginiz metini giriniz :";
    cin.ignore();
    getline(cin,metin);

    int uzunluk = metin.length();

    int fib[max_size]={1,1};

    for(int i=0;i<uzunluk;i++)
    {
        fib[i+2]=fib[i]+fib[i+1];
        cout<<fib[i]<<endl;
        char harf=metin[i];
        int ascii=(int)metin[i];
        int toplanmis=fib[i]+ascii;
        sifre += (char)toplanmis;

    }
    return sifre;
}

string fibonacc_coz()
{
    string metin,sifre;
    cout<<"cozmek istediginiz metni giriniz : ";
    cin.ignore();
    getline(cin,metin);
    int uzunluk=metin.length();
    
    int fib[max_size]={1,1};
    for (int i=0;i<uzunluk;i++)
    {
        fib[i+2]=fib[i]+fib[i+1];
        char harf=metin[i];
        int ascii=(int)harf;
        int toplanmis=ascii-fib[i];
        sifre +=(char)toplanmis;

    }
    return sifre;

}