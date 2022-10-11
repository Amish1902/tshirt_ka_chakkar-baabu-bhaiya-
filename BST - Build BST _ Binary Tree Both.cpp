#include<bits/stdc++.h>
using namespace std;

class Node{
	public: 
		int data;
		Node* left;
		Node* right;
		Node(int d){
			data=d;
			left=NULL;
			right=NULL;
		}
};


void BFSPrint(Node* root){
	if(root==NULL)
		return ;
		queue<pair<Node*,int> > q;
		q.push(make_pair(root,0));
		int level=-1;
		
		while(!q.empty()){
			pair<Node* ,int> p=q.front();
			q.pop();
			Node* n=p.first;
			int l=p.second;
			
			if(n->left)
				q.push(make_pair(n->left,l+1));
			if(n->right)
			q.push(make_pair(n->right,l+1));
			
			if(l>level){
				cout<<"\n";
				level=l;
			}
			cout<<n->data<<" ";
			
			
		}
		
}


//This is Building Binary tree and not BST
Node* BinaryTree(Node* root){
	int d;
	cin>>d;
	if(d==-1)
		return NULL;
	 
	Node* newNode=new Node(d);
	newNode->data=d;
	newNode->left=BinaryTree(newNode->left);
	newNode->right=BinaryTree(newNode->right);
	return newNode;
}

//Inserting one value in BST
Node* InsertBST(Node* root,int d){
	if(root==NULL){
		Node* newNode=new Node(d);
		newNode->data=d;
		newNode->left=NULL;
		newNode->right=NULL;
		return newNode;
	}
	
	if(d<=root->data)
		root->left=InsertBST(root->left,d);
	else
		root->right=InsertBST(root->right,d);
	
	return root;
}

//Building BST
Node* BST(Node* root){
	int d;
	cin>>d;
	while(d!=-1){
		root=InsertBST(root,d);
		cin>>d;
	}
	return root;
}

int main(){
	Node* root1=NULL;
	Node* root2 =NULL;
	
	cout<<"Input For Binary Tree: \n";   //Input: 5 7 1 -1 -1 -1 3 6 -1 -1 8 -1 -1
	root1=BinaryTree(root1);
	 
	cout<<"Input For BST: \n";   //Input: 5 7 3 1 6 8 -1
	root2=BST(root2);
	
	cout<<"\nBinarytree:";  
	BFSPrint(root1);
	cout<<" \n\nBST:";
	BFSPrint(root2);
	
	return 0;
}
