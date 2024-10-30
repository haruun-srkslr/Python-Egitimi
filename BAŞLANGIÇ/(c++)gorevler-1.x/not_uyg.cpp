#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

void not_sil();

void not_oku();

void not_yaz();

int main()
{
    while (true)
    {
    don1:
        cout<<"---------NOT UYGULAMASI---------"<<endl;
        cout<<"1)not yaz"<<endl;
        cout<<"2)not oku"<<endl;
        cout<<"3)not sil"<<endl;
        cout<<"4)Cikis"<<endl;
        cout<<"Seciminizi yapiniz !"<<endl;
        int choice;
        if(!(cin>>choice))
        {
            cout<<"hatali veri tipi girdiniz !"<<endl;
            cin.clear();
            cin.ignore(1000,'\n');
            goto don1;
        }
        switch (choice)
        {
        case 1:not_yaz();break; 
        case 2:not_oku();break; 
        case 3:not_sil();break;           
        case 4:cout<<"Cikiliyor...."<<endl;return 0;
        default:cout<<"hatali secim yaptiniz"<<endl;goto don1;
            break;
        }

        
    }
    
    
}

void not_yaz()
{
    cin.ignore();
    string girilen_yazi;
    cout<<"Eklemek istediginiz yaziyi giriniz : ";
    getline(cin,girilen_yazi);

    if(!girilen_yazi.empty())
    {
        ofstream file("notlar.txt", ios::app);
        
        if (file.is_open())
        {
            file<<girilen_yazi<<endl;
            
            cout<<"notunuz eklendi"<<endl;
            file.close();
        }
    else
    {
        cout<<"bos  not girilemez"<<endl;

    }    

    }


}

void not_oku()
{
    string satir="";
    ifstream file("notlar.txt");
    if (file.is_open())
    {
        int i=1;
        while (getline(file,satir))
        {
           
           cout<<i<<" : "<<satir<<endl;
           i++;
        }

    file.close();
    }

}
void not_sil()
{
    ifstream file("notlar.txt");
    if(!file.is_open())
    {
        cout<<"Dosya bulunamadi"<<endl;
        return;
    }
    vector<string> satirlar;
    string satir;
    int i=1;
    while (getline(file,satir))
    {
        
        cout<<i<<" : "<<satir<<endl;
        satirlar.push_back(satir);
        i+=1;
    }
    file.close();

    if (satirlar.empty())
    {
        cout<<"satirlar bos"<<endl;
        return;
    }
don1:
    cout<<"silinecek satir sayisini giriniz"<<endl;
    cout<<"Numara : ";
    int num;
    if(!(cin>>num))
    {
        cout<<"hatali veri tipi girdiniz"<<endl;
        cout<<"-----------------------------------------"<<endl; 
        cin.clear();
        cin.ignore(1000,'\n');
        goto don1;
    }
    else if(num<1 ||num>satirlar.size())
    {
        cout<<"hatali satir sayisi girdiniz"<<endl;
        cout<<"-----------------------------------------"<<endl; 
        goto don1;
    
       

    }
    else{
        satirlar.erase(satirlar.begin()+num-1);
    }
    ofstream output("notlar.txt");
    if(!output.is_open())
    {
        cout<<"hata olustu"<<endl;
        return;
    }
    for (const auto& s : satirlar) {
        output<<s<<endl;
        
    }



}