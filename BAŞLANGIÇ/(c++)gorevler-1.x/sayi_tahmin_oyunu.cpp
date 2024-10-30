#include<iostream>
#include<ctime>
using namespace std;
void kolay();
void orta();
void zor();
int main()
{
    int sayi,i,choice;
    cout<<"sayi tahmin oyununa hoşgeldiniz"<<endl;
    cout<<"1-KOLAY(1-10)"<<endl;
    cout<<"2-ORTA(1-100)"<<endl;
    cout<<"3-ZOR (1-1000)"<<endl;
    cout<<"secim yapiniz : ";
    cin>>choice;
    switch (choice)
    {
    case 1: kolay(); break;
    case 2: orta(); break;
    case 3: zor(); break;
    default:cout<<"hatali secim yaptiniz"<<endl;break;
    }

}
void kolay()
{
    srand(time(0));
    int tahmin;
    int sayi=rand()%10+1;
    // cout<<sayi<<endl;
    while (true)
    {
    don1:
        cout<<"sayi giriniz : ";
        if(!(cin>>tahmin))
        {
            cout<<"hatali veri girdiniz !"<<endl;
            cin.clear();
            cin.ignore(1000,'\n');
            goto don1;
        }
        if (tahmin<sayi)
        {
            cout<<"daha buyuk "<<endl;
        }
        else if (tahmin>sayi)
        {
            cout<<"daha kucuk"<<endl;
        }
        else if(tahmin==sayi)
        {
            cout<<"dogru tahmin sayi :"<<tahmin<<endl;
            break;
        }
    }
}

void orta()
{
    srand(time(0));
    int sayi=rand()%100+1;
    int tahmin;
    while (true)
    {
    don1:
        cout<<"tahmininizi giriniz";
        if (!(cin>>tahmin))
        {
            cout<<"gecersiz veri tipi girdiniz"<<endl;
            cin.clear();
            cin.ignore(1000,'\n');
            goto don1;
        }
        if(tahmin<sayi)
        {
            cout<<"daha buyuk"<<endl;
        }
        else if(tahmin>sayi)
        {
            cout<<"daha kucuk"<<endl;
        }
        else if(sayi==tahmin)
        {
            cout<<"dogru tahmin yaptiniz cevap : "<<sayi<<endl;
            break;
        }
        
    }
}


void zor()
{
    srand(time(0));
    int sayi=rand()%1000+1;
    int tahmin;
    while (true)
    {
    don1:    
        cout<<"tahmin ediniz ";
        if(!(cin>>tahmin))
        {
            cout<<"hatali veri girdiniz !"<<endl;
            cin.clear();
            cin.ignore(1000,'\n');
            goto don1;
        }
        if (tahmin<sayi)
        {
            cout<<"daha buyuk"<<endl;
        }
        else if(tahmin>sayi)
        {
            cout<<"daha kucuk"<<endl;
        }
        else if(sayi==tahmin)
        {
            cout<<"dogru tahmin :"<<sayi<<endl;
            break;
        }
        
    }
    

}