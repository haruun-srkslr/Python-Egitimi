#include<iostream>
#include<math.h>
#include<iomanip>
using namespace std;
float bolme();
int toplama();
int cikarma();
int fakt();
int us_alma();
int modAlma();
int carpma();
int main()
{
    int secim,toplam,cikan,fakto,us,mod,carp;
    float bolum;

    while (true) {
        cout << "Hesap Makinesi\n";
        cout << "1. Toplama\n";
        cout << "2. Cikarma\n";
        cout << "3. Carpma\n";
        cout << "4. Bolme\n";
        cout << "5. Faktoriyel\n";
        cout << "6. Us Alma\n";
        cout << "7. Mod Alma\n";
        cout << "8. Cikis\n";
        cout << "Seciminizi yapin: ";
        cin >> secim;

        switch (secim) {
            case 1:
                toplam=toplama();
                cout<<toplam<<endl;
                break;
            case 2:
                
                cikan=cikarma();
                cout<<cikan<<endl;
                break;
            case 3:
                carp=carpma();
                cout<<carp<<endl;
                break;
            case 4:
                
                bolum=bolme();
                cout<<bolum<<endl;
                break;
            case 5:
                
                fakto=fakt();
                cout<<fakto<<endl;
                break;
            case 6:
                
                us=us_alma();
                cout<<us<<endl;
                break;
            case 7:
                mod=modAlma();
                cout<<mod<<endl;
                break;
            case 8:
                cout << "Programdan cikiliyor...\n";
                return 0;
            default:
                cout << "Gecersiz secim yaptiniz!\n";
                break;
        }
    }
    return 0;
}


int toplama()
{
    string choice;
    float a,sonuc;
    sonuc=0;
    while (true)
    {
    cout<<"toplamak istediğiniz sayiyi giriniz : ";
sayiyaDon:    
    if(!(cin>>a))
    {
        cout<<"hatali veri girdiniz ! "<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto sayiyaDon;
    }
    sonuc+=a;
    cout<<"devam etmek ister misiniz (E/H)";
don1:    
    cin>>choice;
    if (choice=="E" || choice=="e")
    {
        continue;
    }
    else if(choice=="H" || choice=="h")
    {
        break;
    }
    else
    {
        cout<<"hatali secim yaptiniz"<<endl;
        goto don1;
    }
    
    
    }
    
return sonuc;
}



int cikarma()
{
    string choice;
    float a,sonuc;
    sonuc=0;
    while (true)
    {
    cout<<"cikarmak istediğiniz sayiyi giriniz : ";
sayiyaDon:    
    if(!(cin>>a))
    {
        cout<<"hatali veri girdiniz ! "<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto sayiyaDon;
    }
    sonuc-=a;
    cout<<"devam etmek ister misiniz (E/H)";
don1:    
    cin>>choice;
    if (choice=="E" || choice=="e")
    {
        continue;
    }
    else if(choice=="H" || choice=="h")
    {
        break;
    }
    else
    {
        cout<<"hatali secim yaptiniz"<<endl;
        goto don1;
    }
    
    
    }
    
return sonuc;
}


int carpma()
{
    string choice;
    float a,sonuc;
    sonuc=1;
    while (true)
    {
    cout<<"carpmak istediğiniz sayiyi giriniz : ";
sayiyaDon:    
    if(!(cin>>a))
    {
        cout<<"hatali veri girdiniz ! "<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto sayiyaDon;
    }
    sonuc*=a;
    cout<<"devam etmek ister misiniz (E/H)";
don1:    
    cin>>choice;
    if (choice=="E" || choice=="e")
    {
        continue;
    }
    else if(choice=="H" || choice=="h")
    {
        break;
    }
    else
    {
        cout<<"hatali secim yaptiniz"<<endl;
        goto don1;
    }
    
    
    }
    
return sonuc;
}


float bolme()
{

    float x,y,sonuc;
don1:    
    cout<<"1. sayiyi giriniz : ";
    if(!(cin>>x))
    {
        cout<<"hatali secim yaptiniz !"<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don1;
    }
don2:
    cout<<"2. sayiyi giriniz : ";
    if(!(cin>>y))
    {
        cout<<"hatali secim yaptiniz !"<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don2;
    }
    if (y==0)
    {
        cout<<"y \'ye 0 değerini veremezsiniz ! "<<endl;
        goto don2;
    }
    sonuc=x/y;
    
    return sonuc;


}

int fakt()
{
    int sayi,sonuc;
    sonuc=1;
don1:    
    cout<<"kacin faktoriyeli alinacak : ";
    if(!(cin>>sayi))
    {
        cout<<"hatali veri tipi girdiniz !"<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don1;
    }
    if(sayi<0)
    {
        cout<<"negatif sayilarin faktoriyeli alinamaz !"<<endl;
        goto don1;
    }
    else if (sayi==0)
    {
        sonuc = 1;
        
    }
    if (sayi>0)
    {
        for(int i=1;i<=sayi;i++)
        {
            
            sonuc*=i;

        }

    }


return sonuc;


}

int us_alma()
{
    int b,a,sonuc;
don1:
    cout<<"ussunu almak istediginiz sayiyi giriniz : ";
    if(!(cin>>a))
    {
        cout<<"hatali veri tipi girdiniz !"<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don1;
    }
don2:    
    cout<<a<<" sayisinin ussunu giriniz : ";
    if(!(cin>>b))
    {
        cout<<"hatali veri tipi girdiniz !"<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don2;
    }
    sonuc=pow(a,b);
    return sonuc;

}

int modAlma()
{
    int a,b,sonuc;
don1:
    cout<<"modunu almak istediginiz sayiyi giriniz : ";
    if(!(cin>>a))
    {
        cout<<"hatali veri tipi girdiniz !"<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don1;
    }
don2:    
    cout<<"mod almak istediginiz sayiyi giriniz : ";
    if(!(cin>>b))
    {
        cout<<"hatali veri tipi girdiniz !"<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don2;
    }
    if(b==0)
    {
        cout<<"0\'a bolme yapilamaz ! "<<endl;
        goto don2;
    }
    
    
    sonuc=a % b;
    return sonuc;










}    

