#include <iostream>
using namespace std;

class Queue{
    int *data;
    int front, rear, capacity;
    public:
        Queue(int size){
            data = new int[size];
            front = rear = -1;
            this->capacity = size;
        }

        void enqueue(int value){
            if((rear+1)%capacity == front){
                cout << "Queue is full" << endl;
                return;
            }
            if(front == -1){
                front = 0;
            }
            rear = (rear+1)%capacity;
            data[rear] = value;
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
                front = (front+1)%capacity;
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
            return (rear+1)%capacity == front;
        }

        void display(){
            if(front == -1){
                cout << "Queue is empty" << endl;
                return;
            }
            if(front <= rear){
                for(int i = front; i <= rear; i++){
                    cout << data[i] << " ";
                }
            }else{
                for(int i = front; i < capacity; i++){
                    cout << data[i] << " ";
                }
                for(int i = 0; i <= rear; i++){
                    cout << data[i] << " ";
                }
            }
            cout << endl;
        }
};

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
