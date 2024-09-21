
import sys
import os

# Add the parent directory of `www` (which is `ziggy`) to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# To run Jarvis
import multiprocessing


def startJarvis():
        # Code for process 1
        print("Process 1 is running.")              
        
        from main import start
        start()


# To run hotword
def listenHotword():
        # Code for process 2
        print("Process 2 is running.")
        from www.engine.features import hotword
        hotword()


    # Start both processes
if __name__ == '__main__':
        p1 = multiprocessing.Process(target=startJarvis)
        p2 = multiprocessing.Process(target=listenHotword)
        p1.start()
        p2.start()
        p1.join()

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("system stop")
        