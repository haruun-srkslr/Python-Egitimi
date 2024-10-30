#include<iostream>
#include<vector>
#include<fstream>
#include<sstream>
#include<chrono>

using namespace std;

vector<int> dosya_oku()
{
    try
    {
        vector<int> sayilar;
        string satirlar,filename,c;
        cout<<"dosya adi giriniz : ";
        cin>>filename;
        ifstream file(filename);
        if (file.is_open())
        {
            getline(file,satirlar);
            istringstream iss(satirlar);
            string str_num;

            while(getline(iss,str_num,',')){
                int num=stoi(str_num);
                sayilar.push_back(num);
            }       
            return sayilar;
            file.close();              
        }
        else
        {
            return sayilar;
        }
        
    }
    catch(const exception& e)
    {
        cerr << e.what() << '\n';
    }

}
pair<vector<vector<int>>, double> selection_sort(vector<int>& dizi) 
{
    vector<vector<int>> steps;
    auto start = chrono::high_resolution_clock::now();

    for (size_t i = 0; i < dizi.size(); ++i) 
    {
        for (size_t j = i + 1; j < dizi.size(); ++j) 
        {
            if (dizi[j] < dizi[i]) 
            {
                swap(dizi[i], dizi[j]);
            }
        }
        steps.push_back(dizi);
    }

    auto end = chrono::high_resolution_clock::now();
    double süre = chrono::duration<double>(end - start).count();
    return {steps, süre};
}

pair <vector<vector<int>>,double> bubble_sort(vector<int>& dizi)
{
    double totalTime;
    auto start_time=chrono::high_resolution_clock::now();
    vector<vector<int>> bubble;

    for(int j=0;j<dizi.size();j++)
    {
        for(int i=0;i<dizi.size()-j-1;i++)
        {
            if(dizi[i]>dizi[i+1])
            {
                swap(dizi[i], dizi[i+1]);
            }
        
        }
        bubble.push_back(dizi);
        auto end_time=chrono::high_resolution_clock::now();
        
        totalTime=chrono::duration<double>(end_time-start_time).count();
        // for(auto& c : dizi)
        // {
        //     cout<<c<<" ";
        //     cout<<endl;
        // }
        
   
    }
    return {bubble,totalTime};

}

void dosya_kayıt(const vector<vector<int>>& dizi1, const vector<vector<int>>& dizi2, double süre1, double süre2) {
    try {
        ofstream file("compare.txt", ios::app);
        if (!file.is_open()) 
        {
            throw runtime_error("Dosya açılamadı!");
        }
        
        file << "Bubble Sort\n";
        for (const auto& step : dizi1) 
        {
            for (int num : step) 
            {
                file << num << " ";
            }
            file << endl;
        }
        file << "Süre: " << fixed << süre1 << " saniye\n";
        file << "-----------------------------------------------\n";
        
        file << "Selection Sort\n";
        for (const auto& step : dizi2) 
        {
            for (int num : step) 
            {
                file << num << " ";
            }
            file << endl;
        }
        file << "Süre: " << fixed << süre2 << " saniye\n";
        
    } 
    catch (const exception& e) {
        
        cerr << "Hata: " << e.what() << endl;
    }
}
    
    
    
    









int main()
{
    try
    {

    vector<int> dizi=dosya_oku();
    if (dizi.empty()) 
    {
        cerr << "Hata: Dosyadan veri okunamadi veya dosya bos!" << endl;
        return 1; 
    }
        vector<int> bubble = dizi;
        vector<int> selection = dizi;

        auto [dizi1, süre1] = bubble_sort(bubble);
        auto [dizi2, süre2] = selection_sort(selection);
        
        dosya_kayıt(dizi1, dizi2, süre1, süre2);

        cout << "Sıralama işlemi tamamlandı, sonuçlar 'compare.txt' dosyasına kaydedildi." << endl;
    }
    catch (const exception& e) 
    {
        cerr << "Hata oluştu: " << e.what() << endl;
    }
    return 0;

}