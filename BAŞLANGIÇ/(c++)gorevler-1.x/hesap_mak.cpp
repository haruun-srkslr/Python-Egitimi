#include<iostream>
#include<math.h>
using namespace std;

void uzunluk();
void sicaklik();
void agirlik();
int main()
{
    int choice;
    cout<<" BIRIM DONUSTURUCUYE HOSGELDINIZ"<<endl;
    cout<<"1.UZUNLUK"<<endl;
    cout<<"2.SICAKLIK"<<endl;
    cout<<"3.AGIRLIK"<<endl;
    cout<<"secim yapiniz";
    cin>>choice;
    switch (choice)
    {
    case 1 : uzunluk(); break;
    case 2 : sicaklik(); break;
    case 3 : agirlik();break;
    default : cout<<"hatali secim yaptiniz !";
    }
}

void uzunluk()
{
    int b1,b2;
    float olcu,sonuc;
don1:
    cout << "Cevrilmesi istenen birimi giriniz (1-7 arasi):\n";
    cout << "1. Milimetre\n2. Santimetre\n3. Desimetre\n4. Metre\n5. Dekametre\n6. Hektometre\n7. Kilometre\n";
    cout << "Lutfen bir secim yapiniz: ";
    // cin >> b1;
    
    if(!(cin>>b1))
    {
        cout<<"gecersiz tipte veri girdiniz"<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        cin.clear();
        goto don1;



    }
    else if (b1 < 1 || b1 > 7 )
    {
        cout<<"gecersiz secenek girdiniz"<<endl;
        goto don1;
    }
    
    


don2:    
    cout << "Cevirmek istediginiz birimi giriniz (1-7 arasi):\n";
    cout << "1. Milimetre\n2. Santimetre\n3. Desimetre\n4. Metre\n5. Dekametre\n6. Hektometre\n7. Kilometre\n";
    cout << "Lutfen bir secim yapiniz: ";

    
    if(!(cin>>b2))
    {
        cout<<"gecersiz veri tipi girdiniz ! "<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don2;

    }
    
    else if (b2 < 1 || b2 > 7 )
    {
        cout<<"gecersiz secenek girdiniz"<<endl;
      
    }
    cout<<"olcu giriniz : ";
    cin>>olcu;
    int ust = abs(b2 - b1);
    if (b2 > b1) {
        sonuc = olcu / pow(10, ust);
    } else if (b1 > b2) {
        sonuc = olcu * pow(10, ust);
    } else {
        cout << "Ayni birim!" << endl;
        return;
    }

    cout << "Sonuc: " << sonuc << endl;
}

void sicaklik()
{
    int b1, b2;
    double der, sonuc;
don1:
    cout << "Cevrilmesi istenen sicaklik birimini giriniz (1-3 arasi):\n";
    cout << "1. Celsius\n2. Fahrenheit\n3. Kelvin\n";
    cout << "Lutfen bir secim yapiniz: ";

    if(!(cin>>b1))
    {
        cout<<"gecersiz veri tipi girdiniz "<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don1;

    }
    else if (b1<1 || b1>3)
    {
        cout<<"gecersiz secenek girdiniz ! "<<endl;
        goto don1;


    }
don2:
    cout << "Cevirim yapmak istediginiz birimi giriniz (1-3 arasi):\n";
    cout << "1. Celsius\n2. Fahrenheit\n3. Kelvin\n";
    cout << "Lutfen bir secim yapiniz: ";
    if (!(cin >> b2))
    {
        cout<<"gecersiz veri tipi girdiniz "<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don2;

    }

    else if (b2 < 1 || b2 > 3) {
        cout << "Gecersiz secenek girdiniz!" << endl;
        goto don2;
    }
    
don3: 
    cout << "Dereceyi giriniz: ";
    if (!(cin >> der))
    {
        cout<<"gecersiz veri tipi girdiniz "<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don3;

    }
    if (b1 == 1 && b2 == 2) {
        sonuc = der * 1.8 + 32;
    } else if (b1 == 2 && b2 == 1) {
        sonuc = (der - 32) / 1.8;
    } else if (b1 == 1 && b2 == 3) {
        sonuc = der + 273.15;
    } else if (b1 == 3 && b2 == 1) {
        sonuc = der - 273.15;
    } else if (b1 == 2 && b2 == 3) {
        sonuc = der + 457.87;
    } else if (b1 == 3 && b2 == 2) {
        sonuc = der - 457.87;
    } else {
        cout << "Ayni birim!" << endl;
        return;
    }

    cout << "Sonuc: " << sonuc << endl;
}


void agirlik()
{
    int b1, b2;
    double olcu;
don1:
    cout << "Cevrilmesi istenen agirlik birimini giriniz (1-6 arasi):\n";
    cout << "1. Ton\n2. Kental\n3. Kilogram\n4. Hektogram\n5. Dekagram\n6. Gram\n";
    cout << "Lutfen bir secim yapiniz: ";
    if (!(cin >> b1))
    {
        cout<<"gecersiz veri tipi girdiniz ! "<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don1;
    }


    else if (b1 < 1 || b1 > 6) {
        cout << "Gecersiz secenek girdiniz!" << endl;
        goto don1;
    }
don2:
    cout << "Cevrilmesi istenen agirlik birimini giriniz (1-6 arasi):\n";
    cout << "1. Ton\n2. Kental\n3. Kilogram\n4. Hektogram\n5. Dekagram\n6. Gram\n";
    cout << "Lutfen bir secim yapiniz: ";
    if (!(cin >> b2))
    {
        cout<<"gecersiz veri tipi girdiniz ! "<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don2;
    }


    else if (b2 < 1 || b2 > 6) {
        cout << "Gecersiz secenek girdiniz!" << endl;
        goto don2;
    }
don3:
    cout<<"olcu giriniz : ";
    if(!(cin>>olcu))
    {
        cout<<"gecersiz veri tipi girdiniz ! "<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don3;

    }
    else if(olcu<0)
    {
        cout<<"olcu sıfırdan kucuk olamaz !"<<endl;
        goto don3;
    }

    double sonuc;
    int ust = abs(b2 - b1);
    if (b1 > b2) {
        sonuc = olcu / pow(10, ust);
    } else if (b2 > b1) {
        sonuc = olcu * pow(10, ust);
    } else {
        cout << "Ayni birim!" << endl;
        return;
    }

    cout << "Sonuc: " << sonuc << endl;

}