#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<random>
using namespace std;

vector<string> yanitlar()
{
    try
    {
        vector<string> yanitlar;
        string satirlar;
        ifstream file("yanitlar.txt");
        if (file.is_open())
        {
            
            while (getline(file,satirlar))
            {
                yanitlar.push_back(satirlar);
            }
        }
        return yanitlar;
        
    }
    catch(const exception& e)
    {
        cerr << e.what() << '\n';
    }

}
string rast(vector<string>& eleman)
{
    int rastgele_cevap;
    srand(time(0));
    int elemanSayisi=eleman.size();
    rastgele_cevap=rand() % elemanSayisi + 1;
    return eleman[rastgele_cevap];

}

void yanit_ekle()
{
    try
    {
        string yeni_yanit;
        cout<<"yeni yanitinizi giriniz : ";
        getline(cin,yeni_yanit);
        ofstream file("yanitlar.txt", ios::app);
        if(file.is_open())
        {
            file<<yeni_yanit<<endl;
        }

        
    }
    catch(const exception& e)
    {
        cerr << e.what() << '\n';
    }
}
void dosya_yaz(string soru,string cevap)
{
    try
    {
        ofstream file("magic-8-ball.txt", ios::app);
        if (file.is_open())
        {
            file<<soru<<" : "<<cevap<<endl;
            file<<"-----------------------"<<endl;
        }
        file.close();
        
    }
    catch(const exception& e)
    {
        cerr << e.what() << '\n';
    }
    
    

}







int main()
{
while (true)
{
    string c,cevap,soru;
    vector<string> yanitlar1;
    cout<<"<<<<<<<<<<<<<<<<<<<<<<--------- MAGIC 8 BALL ------>>>>>>>>>>>>>>>>>>>>>>>>>>>"<<endl;
    cout<<"<<<<<<<<<<<<<<<<<<<<<<--------- HOSGELDINIZ  ------>>>>>>>>>>>>>>>>>>>>>>>>>>>"<<endl;
    cout<<"                    !!CIKIS YAPMAK ICIN Q&q YAZINIZ!!                         "<<endl;
    cout<<"                 !!YENI YANITLAR EKLEMEK ICIN \'I\' TUSUNA BASINIZ!           "<<endl;

    yanitlar1 = yanitlar();
    cout<<"sorunuzu sorunuz : ";
    getline(cin,soru);
    cevap=rast(yanitlar1);
    if(soru=="Q"||soru=="q")
    {
        cout<<"cikiliyor..."<<endl;
        break;

    }
    if (soru=="I"||soru=="ı")
    {
        yanit_ekle();
    }
    else
    {
    
    dosya_yaz(soru,cevap);
    cout<<cevap<<endl;
    }
    
}










}