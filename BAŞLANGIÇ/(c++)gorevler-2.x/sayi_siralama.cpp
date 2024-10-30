#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>

using namespace std;

vector<int> dosya_okuma(string& filename)
{
    vector<int> sayilar;
    string satirlar,kelime;
    try
    {   
        ifstream file(filename);
        if (file.is_open())
        {
            
            getline(file,satirlar);
            istringstream iss(satirlar);
            string str_num;
            while(getline(iss,str_num,','))
            {
                int num=stoi(str_num);
                sayilar.push_back(num);
     
            }
            return sayilar;
            file.close();
 
        }
        
        else
        {
            cout<<"bir hata olustu"<<endl;
            return sayilar;
        }

    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }

}

vector<int> siralama(vector<int> sayis)
{
    
    vector<int> vect2;
    vect2=sayis;
    sort(vect2.begin(),vect2.end(),greater<int>());
    for(auto a:vect2)
    {
        cout<<a<<endl;
    }
    cout<<vect2[0]<<" "<<vect2[vect2.size()-1]<<endl;
    int enBuyuki=vect2[0];
    int enKucuki=vect2[vect2.size()-1];
    auto it=find(sayis.begin(),sayis.end(),enBuyuki);
    int index1 = distance(sayis.begin(), it);
    auto it1=find(sayis.begin(),sayis.end(),enKucuki);
    int index2 = distance(sayis.begin(), it1);
    cout<<index1<<endl;
    cout<<index2<<endl;
    ofstream file("report.txt", ios::app);
    if(file.is_open())
    {
        for (auto a:vect2){
        file<<a<<",";
        }
        file<<endl;
        file<<"en buyuk sayi --> "<<vect2[0]<<" indexi --> "<<index1<<" sirasi --> "<<index1+1<<endl;
        file<<"en kucuk sayi --> "<<vect2[vect2.size()-1]<<" indexi --> "<<index2<<" sirasi --> "<<index2+1<<endl;
        file<<"----------------------------------------------------------------------"<<endl;
        cout<<"\"report.txt\" dosyasinin icine kayit edildi ."<<endl;
    }






}



















int main()
{
    vector<int> sayilar;
    
    string filename;
    cout<<"dosya adi giriniz";
    cin>>filename;
    sayilar=dosya_okuma(filename);
    siralama(sayilar);
    
   
        
    
    

}