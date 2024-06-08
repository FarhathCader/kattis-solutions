#include <iostream>
using namespace std;

class Queue{
    private:
        int front;
        int rear;
        int *data;
        int capacity;
    public:
        Queue(int size){
            data = new int[size];
            front = rear = -1;
            this->capacity = size;
        }

        void enqueue(int value){
            if(rear == capacity-1){
                cout << "Queue is full" << endl;
                return;
            }
            data[++rear] = value;
            if(front == -1){
                front = 0;
            }
        }

        int dequeue(){
            if(front == -1){
                cout << "Queue is empty" << endl;
                return -1;
            }
            int value = data[front];
            if(front == rear){
                front = rear = -1;
            }else{
                front++;
            }
            return value;
        }

        int peek(){
            if(front == -1){
                cout << "Queue is empty" << endl;
                return -1;
            }
            return data[front];
        }

        bool isEmpty(){
            return front == -1;
        }

        bool isFull(){
            return rear == capacity-1;
        }

        void display(){
            if(front == -1){
                cout << "Queue is empty" << endl;
                return;
            }
            for(int i = front; i <= rear; i++){
                cout << data[i] << " ";
            }
            cout << endl;
        }


      
      
}

int main(){
    Queue queue(5);
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    queue.enqueue(4);
    queue.enqueue(5);
    queue.enqueue(6);
    queue.display();
    cout << queue.dequeue() << endl;
    cout << queue.dequeue() << endl;
    cout << queue.peek() << endl;
    queue.display();
    return 0;
}