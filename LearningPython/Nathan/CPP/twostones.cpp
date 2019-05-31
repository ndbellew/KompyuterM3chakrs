#include <iomanip>
#include <iostream>
#include <string>
using namespace std;

class twostones{
	public:
	string printWinner(int stones){
		if (stones%2 == 0)
			return "Bob";
		else
			return "Alice";
		return "FAIL";
	}
	
	
};

int main(){
	twostones stones;
	
	int N;
	cin>>N;
	
	string winner = stones.printWinner(N);
	cout << winner<<endl;
	return 0;
}
