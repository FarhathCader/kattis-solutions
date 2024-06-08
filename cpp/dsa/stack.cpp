#include <iostream>
using namespace std;

class Stack{
    private:
        int top;
        int *data;
        int size;
    public:
        Stack(int size){
            this->size = size;
            data = new int[size];
            top = -1;
        }
        void push(int value){
            if(top == size-1){
                std::cout << "Stack is full" << std::endl;
                return;
            }
            data[++top] = value;
        }
        int pop(){
            if(top == -1){
                std::cout << "Stack is empty" << std::endl;
                return -1;
            }
            return data[top--];
        }
        int peek(){
            if(top == -1){
                std::cout << "Stack is empty" << std::endl;
                return -1;
            }
            return data[top];
        }
        bool isEmpty(){
            return top == -1;
        }
        bool isFull(){
            return top == size-1;
        }
        void display(){
            if(top == -1){
                std::cout << "Stack is empty" << std::endl;
                return;
            }
            for(int i = top; i >= 0; i--){
                std::cout << data[i] << " ";
            }
            std::cout << std::endl;
        }
        ~Stack(){
            delete[] data;
        }
}

int main(){
    Stack stack(5);
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);
    stack.push(5);
    stack.push(6);
    stack.display();
    std::cout << stack.pop() << std::endl;
    std::cout << stack.pop() << std::endl;
    std::cout << stack.peek() << std::endl;
    stack.display();
    return 0;
}