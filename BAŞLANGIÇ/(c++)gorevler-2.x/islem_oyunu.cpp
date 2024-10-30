#include<iostream>
#include<vector>
#include<fstream>
#include<cmath>

using namespace std;



string rastgele_islem()
{
    vector<string> isaret ={"arti","eksi","bolme","carpma"};
    srand(time(0));
    string rastgele_islem=isaret[rand()%4+0];
    cout<<rastgele_islem<<endl;
    return rastgele_islem;
}









int islem_yazma_kontrol(string islem)
{
    
        int cevap;
        srand(time(0));
        
        if (islem=="arti")
        {
            int sayi1=rand()%10+1;
            int sayi2=rand()%10+1;
            int cev=sayi1+sayi2;
            cout<<sayi1<<"+"<<sayi2<<"= ?"<<endl;
            return cev;
            
        }
        else if (islem=="eksi")
        {
            int sayi1=rand()%10+1;
            int sayi2=rand()%10+1;
            int cev=sayi1-sayi2;
            cout<<sayi1<<"-"<<sayi2<<"= ?"<<endl;
            return cev;
            
        }
        else if(islem=="bolme")
        {
            while (true)
            {
            
            int sayi1=rand()%10+1;
            int sayi2=rand()%10+1;
            int cev=sayi1/sayi2;
            if (floor(cev)==cev)
            {
                cout<<sayi1<<"/"<<sayi2<<" = ? "<<endl;
                return cev;
            }
            else
            {
                cout<<"yeni sayi seciliyor bekleyiniz"<<endl;
            }
            }
        }
        else if (islem=="carpma")
        {
            int sayi1=rand()%10+1;
            int sayi2=rand()%10+1;
            int cev=sayi1*sayi2;
            cout<<sayi1<<"*"<<sayi2<<"= ?"<<endl;
            return cev;
            
        }

    
}

void dosya_kayit(int dogrus,int yanliss)
{
    try
    {
        ofstream file("sonuc_raporlari.txt",ios::app);
        if(file.is_open())
        {
            file<<"dogru sayisi : "<<dogrus<<endl;
            file<<"yanlis sayisi : "<<yanliss<<endl;
            file<<"-------------------------------------"<<endl;

        }









    }
    catch(const exception& e)
    {
        cerr << e.what() << '\n';
    }
    
}












int main()
{
    int dogrus=0;
    int yanliss=0;
    while (true)
    {
        cout<<"oyundan cikmak icin \" 9999 \" yaziniz"<<endl;
        string islem=rastgele_islem();
        int cevap=islem_yazma_kontrol(islem);
    don1:
        int kcevap;
        if(!(cin>>kcevap))
        { 
            cout<<"hatali veri tipi girdiniz"<<endl;
            cin.clear();
            cin.ignore(1000,'\n');
            goto don1;
        }
        if (kcevap==9999)
        {
            break;
        }
        if (kcevap==cevap)
        {
            dogrus+=1;
            cout<<dogrus<<endl;
            cout<<yanliss<<endl;
            dosya_kayit(dogrus,yanliss);
        }
        else if (kcevap!=cevap)
        {
            yanliss+=1;
            cout<<dogrus<<endl;
            cout<<yanliss<<endl;
            dosya_kayit(dogrus,yanliss);
        }
        
        
    
    
    
    
    
    
    
    
    
    
    }
    
    


}