#include<iostream>
#include<fstream>

using namespace std;
string atbash_sifreleme(string& metin);
void dosya_yaz(string& input,string& cikti);
int main()
{
    string cc,sifreleme,metin;
    while (true) 
    {
            cout << "\n<<<<<<<<<<<< ATBASH SIFRELEME >>>>>>>>>>>>>>>>>>\n";
            cout << "1) SIFRELEME\n";
            cout << "2)CIKIS\n";
            cout << "Secim yapiniz: ";
        
        int choice;
        if(!(cin>>choice))
        {
            cout<<"hatali secim yaptiniz ! "<<endl;
            cin.clear();
            cin.ignore(1000,'\n');
            continue;

        }
        cin.ignore();
        switch (choice)
        {
        case 1:
        getline(cin,metin);
        sifreleme=atbash_sifreleme(metin);
        cout<<sifreleme<<endl;
        dosya_yaz(metin,sifreleme);
        break;
        case 2:return 0;break;
        default:cout<<"hatali secim yaptınız";break;
        }

    }
    
    
}
string atbash_sifreleme(string& metin)
{
    int i,index_num;
    
    char harf;
    string yeni_metin,sifre;
    
    char alfabe[35];
    char ters_alfabe[35];

    for(int b=0;b<metin.length();b++)
    {
        yeni_metin+=tolower(metin[b]);
        

    }

    int uzunluk=yeni_metin.length();
    for(i=0;i<26;i++){
        alfabe[i]='a'+i;
        ters_alfabe[i]='z'-i;
        
        
    }
    for (int j=0;j<uzunluk;j++)
    {
        harf=yeni_metin[j];
        
        bool harfYok=false;
        for (int a=0;a<26;a++)
        {
            if (harf==alfabe[a])
            {
                sifre+=ters_alfabe[a];
                harfYok=true;
                break;
            }
    
        }
        if (!harfYok)
        {
            sifre+=harf;
        }
     
    
    }

    return sifre;
}



void dosya_yaz(string& input,string& cikti)
{
    ofstream file("atbash.txt",ios::app);
    if (!file) {  // Dosya açılamazsa
        ofstream yeni("atbash.txt");
        yeni.close();
        
    }
    else if (file.is_open()){
        file<<input<<"--->"<<cikti<<endl;
        file<<"-------------------------\n";
        file.close();
    }


}