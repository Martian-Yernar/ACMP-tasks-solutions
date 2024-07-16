#include <iostream>
using namespace std;

int main(){
	int n, aInfo;
	cin >> n;
	int sum = 0;
	for (int i = 0; i < n; i++){
		cin >> aInfo;
		sum += aInfo;
	}
	
	cout << sum - n + 1;
	return 0;
}
