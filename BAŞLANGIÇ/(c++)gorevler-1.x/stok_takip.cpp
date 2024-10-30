#include<iostream>
#include<string>

using namespace std;
const int MAX_URUN=100;
string urunler[MAX_URUN];
int stok[MAX_URUN];
int urunSayisi=0;

void azOlan();
void urunListele();
void urunCikar();
void urunEkle();
void menu();
int main()
{
    menu();
    return 0;
}
void menu()
{
    while (true)
    {
        cout << "\n--- STOK TAKIP SISTEMI ---\n";
        cout << "1. URUN EKLE\n";
        cout << "2. URUNLERI LISTELE\n";
        cout << "3. URUN CIKAR\n";
        cout << "4. AZ OLAN URUNLERI LISTELE\n";
        cout << "Q. CIKIS\n";
        cout << "--- SECIM YAPINIZ (1-4/Q) ---: ";
    
        string secim;
        cin >> secim;

        if (secim == "1") 
        {
            urunEkle();
        } 
        else if (secim == "2") 
        {
            urunListele();
        }
        else if (secim == "3") 
        {
            urunCikar();
        } 
        else if (secim == "4") 
        {
            azOlan();
          
        } 
        else if (secim == "Q" || secim == "q")
        {
            cout << "CIKIS YAPILIYOR...\n";
            break;
        } 
        else 
        {
            cout << "HATALI SECIM YAPTINIZ!\n";
        }
    }
}
void urunEkle()
{
    if (urunSayisi>=MAX_URUN)
    {   
        cout<<"stok kapasitesi dolu";
        return;
    }
    string urunAdi;
    int adet;
    cout<<"eklenecek urun adini giriniz : ";
    cin>>urunAdi;
don1:    
    cout<<"kaç adet eklenmesini istersiniz : ";
    if(!(cin>>adet))
    {
        cout<<"hatali veri tipi girdiniz !";
        cin.clear();
        cin.ignore(1000,'\n');
        goto don1;
    }
    if (adet<=0)
    {
        cout<<"urun adedi negatif olamaz !";
        goto don1;
    }
    for(int i=0;i<=urunSayisi;i++)
    {
        if(urunler[i]==urunAdi)
        {
            stok[i]+=adet;
            cout<<"ürün sayisi güncellendi !";
            return;
        }
    }
    urunler[urunSayisi]=urunAdi;
    stok[urunSayisi]=adet;
    urunSayisi+=1;
    cout<<"urun basariyla eklendi"<<endl;
}


void urunListele()
{
    if (urunSayisi==0)
    {
        cout<<"listede urun yok !";
        return;

    }
    cout<<"\n----ÜRÜNLER----\n";
    for(int i=0;i<urunSayisi;i++)
    {
        cout<<urunler[i]<<" : "<<stok[i]<<endl;   
    }
}

void urunCikar()
{
    if(urunSayisi==0)
    {
        cout<<"listede urun yok !";
        return;
    }
    string urunAdi;
    int adet;
    cout<<"cikarilacak urun adini giriniz : ";
    cin>>urunAdi;
    for(int i=0;i<urunSayisi;i++)
    {
        if (urunAdi==urunler[i])
        {
        don1:
            cout<<urunler[i]<<" urununden "<<stok[i]<<" adet vardir kac tane cikarilsin"<<endl;
            if(!(cin>>adet))
            {
                cout<<"hatali veri tipi girdiniz ! ";
                cin.clear();
                cin.ignore(1000,'\n');
                goto don1;
            }
            if (adet<=0)
            {
                cout<<"urun sayisi sifir veya negatif olamaz !";
                goto don1;
            }
            else if(adet>stok[i])
            {
                cout<<"stokta yeteri kadar urun yok olan urun adedi : "<<stok[i]<<endl;
                goto don1;
            }
            stok[i]-=adet;
            if (stok[i]==0)
            {
                for(int j =i;j<urunSayisi-1;j++)
                {
                    urunler[j]=urunler[j+1];
                    stok[j]=stok[j+1];
                }
                urunSayisi-=1;
                cout<<"urun tamamen stoktan cikarildi"<<endl;
            }    
            else
            {
                cout<<adet<<"adet cikarildi";
            }
        }
        return;
        

    }
    cout<<"urun bulunamadı"<<endl;

}


void azOlan()
{
    bool azOlan=false;
    int i;
    for(i=0;i<urunSayisi;i++)
    {
        if (stok[i]<=5)
        {
            cout<<endl<<"----Az Olan Urunler----"<<endl;
            cout<<urunler[i]<<" urununden "<<stok[i]<<"adet kaldı"<<endl;
            azOlan=true;
        }

    }

    if (!azOlan)
    {
        cout<<"stokta az olan urun yok !"<<endl;
    }
    
}