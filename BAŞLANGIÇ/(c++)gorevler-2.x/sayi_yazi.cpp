#include<iostream>
#include<string>
#include<fstream>
#include<vector>
using namespace std;

vector<string> sayi_yaziyla(const vector<int>& sayilar)
{
    vector<string> kelimeler;
    for (int sayi:sayilar)
    {
        
        vector<string> birler = {"","bir","iki", "uc", "dort", "bes", "alti", "yedi", "sekiz", "dokuz"};
        vector<string> onlar = {"","on","yirmi", "otuz", "kirk", "elli", "altmis", "yetmis", "seksen", "doksan"};
        if(sayi==0)
        {
            kelimeler.push_back("sifir");
            return kelimeler;
        }
        if (sayi<0)
        {
            cout<<"sifirdan kücük sayi giremezsiniz !"<<endl;
            exit(1);

        }
        string kelime;
        int milyon=sayi/1000000;
        sayi=sayi-(milyon*1000000);
        if( milyon>0)
        {
            if (milyon==1)
            {
                kelime+=" Bir milyon ";
            }
            else
            {
                kelime+=sayi_yaziyla({milyon})[0]+" milyon ";
            }
        }


        //bin
        int binn=sayi/1000;
        sayi=sayi-(binn*1000);
        if (binn>0)
        {
            if(binn==1)
            {
                kelime+=" bin ";
            }
            else
            {
                kelime+=sayi_yaziyla({binn})[0]+" bin ";

            }
        }
        //yüz
        int yuz=sayi/100;
        sayi=sayi-(yuz*100);
        if (yuz>0)
        {
            if(yuz==1)
            {
                kelime+="yuz";
            }
            else
            {
                kelime+=sayi_yaziyla({yuz})[0]+" yuz ";
            }
        }
        int on=sayi/10;
        sayi=sayi-(on*10);
        if (on>0)
        {
            kelime+=onlar[on]+" ";
        }
        kelime+=birler[sayi]+" ";

        kelimeler.push_back(kelime);
        

    }
    return kelimeler;
}
        
    

vector<int> dosya_okuma()
{
try{
    vector<int> sayilar;
    string filename,satir;
    cout<<"dosya adini giriniz : ";
    cin>>filename;
    ifstream file(filename);
    if(file.is_open())
    {
        while(getline(file,satir))
        {
            int satir1=stoi(satir);
            sayilar.push_back(satir1);            
        
        }

    }
        return sayilar;
}
    catch(const exception& e)
    {
        cerr << e.what() << '\n';
    }    

}

void dosya_yaz(const vector<int>& sayilar,const vector<string>& kelimeler)
{
    try
    {
    string outputName;
    cout<<"cikis dosyasinin adini yaziniz";
    cin>>outputName;
    ofstream file(outputName);
        if (file.is_open())
        {
            for(size_t i=0;i<kelimeler.size();i++)
            {
                file<<sayilar[i]<<"--->"<<kelimeler[i]<<endl;
                file<<"-----------------------------"<<endl;

            }
        }
    }
    catch (const exception& e) {
        cout << "Hata oluştu: " << e.what() << endl;
    }
}









int main()
{
vector<string> kelimeler;
vector<int> sayilar;
sayilar=dosya_okuma();
kelimeler=sayi_yaziyla(sayilar);
dosya_yaz(sayilar,kelimeler);
for(string kelime:kelimeler){
    cout<<kelime<<endl;  

}
return 0;  

}