#include<iostream>
#include<map>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>
using namespace std;






string dosya_okuma(string filename)
{
    try
    {
        string temizKelime;
        
        ifstream file(filename);
        if (file.is_open())
        {
            string satirlar;
            while(getline(file,satirlar))
            {
            istringstream iss(satirlar);
            string kelimeler;
            while(iss>>kelimeler)
            {
                
                for(char  c : kelimeler)
                {
                 if(isalpha(c))
                 {
                    temizKelime+=(char)tolower(c);
                 }   
                }
                if(temizKelime.empty())
                {
                    cout<<"bos dosya "<<endl;
                    return temizKelime;
                }
            }
            }
        


        }
    file.close();
    return temizKelime;
        
    }
    catch(const exception& e)
    {
        cerr << e.what() << '\n';
        return "";
    }
    







}

    
    
    
    
    
vector<pair<char,int>> frekans (const string& metin)
{
    map<char,int> frekans1;
    vector<pair<char,int>> vect;
    for(char harf:metin)
    {
        if(isalpha(harf))
        {
            frekans1[harf]++;
        }
    }
    for (const auto element:frekans1)
    {
        vect.push_back(element);
    }

    vector<pair<char,int>> siralanmis;  
    for(int j=0;j<vect.size();j++)
    {
    for(int i=0;i<vect.size()-j-1;i++)
    {
        if( vect[i].second>vect[i+1].second)
        {
            swap(vect[i], vect[i+1]);
            
        }
    
    }

    }  
    for (auto elem:vect)
    {
        siralanmis.push_back(elem);
    } 
    return siralanmis;


}
void dosya_yazma(vector<pair<char,int>> sonuc,string filename)
{
    try
    {
        ofstream file("frequency_analysis.txt",ios::app);
        if(file.is_open())
        {
            for(auto element:sonuc)
            {
                file<<element.first<<" : "<<element.second<<endl;
                
            }
            file<<"dosya adi : "<<filename<<endl;
            file<<"--------------------------------"<<endl;





        }
        file.close();
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }
    






}

























int main()
{
    string kelimeler,filename;
    cout<<"dosya adini giriniz : ";
    cin>>filename;
    vector<pair<char,int>> sonuc;
 
    kelimeler=dosya_okuma(filename);
    sonuc=frekans(kelimeler);
    dosya_yazma(sonuc,filename);
    return 0;
    
    
    


}