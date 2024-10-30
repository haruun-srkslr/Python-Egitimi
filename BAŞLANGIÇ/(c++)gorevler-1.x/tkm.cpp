#include<iostream>
#include<random>
using namespace std;
void oyna();
void menu();
int main()
{
    menu();


}
void menu()
{
don1:
    while (true)
    {
    cout<<"Tas-Kagit-Makas"<<endl;
    cout<<"1) Oyna"<<endl;
    cout<<"2) Cikis"<<endl;
    int choice;
    if (!(cin>>choice))
    {
        cout<<"hatali veri tipi girdiniz !"<<endl;
        cin.clear();
        cin.ignore(1000,'\n');
        goto don1;
    }
    if(choice==1)
    {
        oyna();

    }
    else if(choice==2)
    {
        break;

    }
    else
    {
        cout<<"hatali secim yaptiniz !"<<endl;
    }
    }
    
}
void oyna()
{
    int kullanici=0;
    int bilgisayar=0;
    int girdi;
    
    while (true)
    {
    don1:
        string tkm[3]={"TAS","KAGIT","MAKAS"};
        cout<<" TAS-KAGIT-MAKAS"<<endl;
        cout<<"1.TAS"<<endl;  
        cout<<"2.KAGIT"<<endl;
        cout<<"3.MAKAS"<<endl;
        cout<<"4.Cikis"<<endl;

        srand(time(0));
        int s1=rand()%3+1;
        if(!(cin>>girdi))
        {
            cout<<"hatali veri tipi girdiniz"<<endl;
            cin.clear();
            cin.ignore(1000,'\n');
            goto don1;
        }
        if(s1==girdi)
        {
            cout<<"beraberlik !"<<endl;
            cout<<"bilgisayarin hamlesi : "<<tkm[s1-1]<<endl;
            cout<<"senin hamlen : "<<tkm[girdi-1]<<endl;
            
        }
        else if((girdi == 1 && s1 == 3) ||
            (girdi == 2 && s1 == 1) ||
            (girdi == 3 && s1 == 2))
            {
                cout<<"Kazandiniz !"<<endl;
                kullanici+=1;
                cout<<"senin hamlen : "<<tkm[girdi-1]<<endl;
                cout<<"bilgisayarin hamlesi : "<<tkm[s1-1]<<endl;
                cout<<"-------SKORLAR-------"<<endl;
                cout<<"kullanici :"<<kullanici<<endl;
                cout<<"bilgisayar : "<<bilgisayar<<endl;

            }
        else if((girdi == 3 && s1 == 1) ||
            (girdi == 1 && s1 == 2) ||
            (girdi == 2 && s1 == 3))
            {
                cout<<"Kaybettiniz !"<<endl;
                bilgisayar+=1;
                cout<<"senin hamlen : "<<tkm[girdi-1]<<endl;
                cout<<"bilgisayarin hamlesi : "<<tkm[s1-1]<<endl;
                cout<<"-------SKORLAR-------"<<endl;
                cout<<"kullanici :"<<kullanici<<endl;
                cout<<"bilgisayar : "<<bilgisayar<<endl;

            }
        else if(girdi ==4)
        {
            if(bilgisayar>kullanici)
            {
                cout<<"Kaybettiniz"<<endl;
                cout<<"kullanici : "<<kullanici<<endl;
                cout<<"bilgisayar : "<<bilgisayar<<endl;
            }
            else if(kullanici>bilgisayar)
            {
                cout<<"Kazandiniz"<<endl;
                cout<<"kullanici : "<<kullanici<<endl;
                cout<<"bilgisayar : "<<bilgisayar<<endl;
            }
            cout<<"Cikiliyor...."<<endl;
            break;
        }
        else
        {
            cout<<"hatali hamle yaptiniz"<<endl;
        }



        
        
        


    }
    







}


