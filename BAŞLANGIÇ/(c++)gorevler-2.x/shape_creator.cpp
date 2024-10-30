#include<iostream>
#include<chrono>
#include<fstream>
using namespace std;




void ucgen_ciz(int satir_sayisi)
{
    try
    {
        auto start_time=chrono::high_resolution_clock::now();
        ofstream file("shapes.txt",ios::app);
        if(file.is_open())
        {
        for(int i=1;i<=satir_sayisi;i++)
        {
            for(int j=1;j<=i;j++)
            {
                cout<<" "<<"*";
                file<<" "<<"*";
            }
            file<<endl;
            cout<<endl;
        }

        auto end_time=chrono::high_resolution_clock::now();
        chrono::duration<double> totaltime=end_time-start_time;
        file<<"sure : "<<totaltime.count()<<"saniye"<<endl;
        file<<"----------------------------------"<<endl;
        file.close();
        }
            
    }
    catch(const exception& e)
    {
        cerr << e.what() << '\n';
    }
}

void dikdortgen_ciz(int satir_say,int sutun_say)
{
    auto start_time=chrono::high_resolution_clock::now();
    ofstream file("shapes.txt",ios::app);
    if(file.is_open())
    {
        for(int i = 1;i<=satir_say;i++)
        {
            for (int j = 1;j<=sutun_say;j++)
            {
                cout<<" "<<"* ";
                file<<" "<<"* ";
            }
            cout<<endl;
            file<<endl;
        }
    auto endTime=chrono::high_resolution_clock::now();
    chrono::duration<double> totalTime=endTime-start_time;
    file<<"sure : "<<totalTime.count()<<endl;
    file<<"-------------------------------------------------------"<<endl;
    file.close();
    }

}
void kare_ciz(int kenar_say)
{
    auto start_time=chrono::high_resolution_clock::now();
    ofstream file("shapes.txt",ios::app);
    if (file.is_open())
    {
        for(int i=1;i<=kenar_say;i++)
        {
            for(int j=1;j<=kenar_say;j++)
            {
                cout<<" "<<"* ";
                file<<" "<<"* ";
            }
        file<<endl;
        cout<<endl;
        }
    auto endTime=chrono::high_resolution_clock::now();
    chrono::duration<double> totalTime=endTime-start_time;
    file<<"sure : "<<totalTime.count()<<endl;
    file<<"--------------------------------------------------"<<endl;
    file.close();

        
    }
    
    
    












}















void menu()
{
    while (true)
    {
        cout<<"<<<<<<< SHAPE CREATOR >>>>>>>"<<endl;
        cout<<"1) Ucgen ciz"<<endl;
        cout<<"2) dikdortgen ciz"<<endl;
        cout<<"3) kare ciz"<<endl;
        cout<<"Q & q) Cikis"<<endl;
        int satir_sayisi;
        string choice;
        cout<<"secim yapiniz";
        cin>>choice;
        if (choice=="1")
        {
            int satir_say;
        don1:
            cout<<"satir sayisi giriniz : ";
            if(!(cin>>satir_say))
            {
                cout<<"hatali veri tipi"<<endl;
                cin.clear();
                cin.ignore(1000,'\n');
                goto don1;
            }
            ucgen_ciz(satir_say);

        }   
        else if (choice=="2")
        {
            int satir_say,sutun_say;
        don2:
            cout<<"satir sayisi giriniz : ";
            if(!(cin>>satir_say))
            {
                cout<<"hatali veri tipi"<<endl;
                cin.clear();
                cin.ignore(1000,'\n');
                goto don2;
            }
        don3:
            cout<<"sutun sayisi giriniz";
            if(!(cin>>sutun_say))
            {
                cout<<"hatali veri tipi"<<endl;
                cin.clear();
                cin.ignore(1000,'\n');
                goto don3;
            }
        dikdortgen_ciz(satir_say,sutun_say);

            
        }
        else if (choice=="3")
        {
             int satir_say;
        don4:
            cout<<"karenin bir kenarini giriniz : ";
            if(!(cin>>satir_say))
            {
                cout<<"hatali veri tipi"<<endl;
                cin.clear();
                cin.ignore(1000,'\n');
                goto don4;
            }
            kare_ciz(satir_say);
            
        }   
        else if (choice=="Q"||choice=="q")
        {
            break;
        }
        else
        {
            cout<<"hatali secim yaptiniz"<<endl;
        }












    }


}

int main()
{
    menu();
}