#include<iostream>
#include<vector>
#include<string>
#include<fstream>

using namespace std;    

vector<string> dosya_okuma()
{
    try
    {
        vector<string> dna;
        string filename,satirlar;
        cout<<"dosya adini giriniz : ";
        cin>>filename;
        ifstream file(filename);
        if(file.is_open())
        {
            while(getline(file,satirlar))
            {
                for(auto &c :satirlar) c=toupper(c);
                dna.push_back(satirlar);

            }


        return dna;
        }
        if(dna.empty()){
            cout<<"Bos dosya"<<endl;
            
        }
    
    file.close();
    return dna;
        
    }
    catch(const exception& e)
    {
        cerr << e.what() << '\n';
    }
}

vector<string> dna_karsilik(const vector<string>& dna)
{
    vector<string> dna1;    
    for(string satir : dna)
    {   
        string yeniSatir;
        for(char i : satir)
        {
            if(i==',')
            {
                continue;
            }
            if(i!='A' && i != 'T' && i!='C' && i!='G')
            {
                cout<<"hatali dna tanimlamasi"<<endl;
                dna1.push_back("hatali dna tanimlamasi");
                break;
            }
            else
            {

            if (i == 'A')
                yeniSatir+='T';
                
            else if (i == 'T')
                yeniSatir+='A';
                
            else if (i == 'G')
                yeniSatir+='C';
                
            else if (i == 'C')
                yeniSatir+='G';
                
            }
            
        }
        dna1.push_back(yeniSatir);


    }
    return dna1;








}
    
void dosya_yazma(vector<string>& dna,vector<string>& sonuc)
{
    ofstream file("output" ,ios::app);
    if (file.is_open()){
    for(int i=0;i<dna.size();i++)
    {
        file<<dna[i]<<"---->"<<sonuc[i]<<endl;
        file<<"-----------------------------"<<endl;



    }
    }
}





int main()
{
    char satir;
    vector<string> dna;
    vector<string> sonuc;
    dna=dosya_okuma();
    sonuc=dna_karsilik(dna);
    for(int i=0;i<sonuc.size();i++)
    {
        cout<<sonuc[i]<<endl;
    }
    dosya_yazma(dna,sonuc);

    
    

}