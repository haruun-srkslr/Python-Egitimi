#include<iostream>
#include<math.h>
using namespace std;

int main()
{
    float delta,kok1,kok2,kokler;
    int a,b,c;
    cout<<"ax^2+bx+c ikinci dereceden denkleminin katsayilarini giriniz : "<<endl;
    while (true)
    {
        cout<<"a : ";
        cin>>a;
        if (cin.fail())
        {
            cout<<"gecersiz giris denemesi "<<endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        else if(a==0)
        {
            cout<<"a katsayisi 0'a esit olamaz ! "<<endl;
        }
        else
        {
            break;
        }

    }
    while(true)
    {
        cout<<"b : ";
        cin>>b;
        if(cin.fail())
        {
            cout<<"gecersiz giris denemesi "<<endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        else
        {
            break;
        }
    }
    while(true)
    {
        cout<<"c: ";
        cin>>c;
        if(cin.fail())
        {
            cout<<"gecersiz giris denemesi"<<endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');

        }
        else
        {
            break;
        }
    }
    
    delta=(pow(b,2)-4*a*c);
    cout<<delta<<endl;
    if (delta>0)
    {
        kok1=(-b+sqrt(delta))/(2*a);
        kok2=(-b-sqrt(delta))/(2*a);
        cout<<"1. kok : "<<kok1<<endl;
        cout<<"2. kok : "<<kok2<<endl;
    }
    if(delta==0)
    {
        kokler=-b/(2*a);
        cout<<"çakisik kokler : "<<kokler<<endl;
    }
    if(delta<0)
    {
        cout<<"reel kok yoktur ! "<<endl;
    }

    return 0;














}