import sys
import tkinter as tk

def verify_environment():
    print(" SHORTEST PATH FINDING IN A MAZE - INITIALIZATION")
    print(f"python version : {sys.version.split()[0]}")   #print the interpreter version

    # check tkinter availability 

    try:
        root=tk.Tk() # creates the main Tkinter application window.
        root.withdraw() # We don't actually want a blank window appearing on the screen.
        print("Tkinter status : Functional")
        root.destroy()
    except Exception as e:
        print(f"Tkinter Status : Failed {e}")
        return False

    # check matplotlib availability

    try:
        import matplotlib
        print(f"Matplotlib      : Installed (v{matplotlib.__version__})")
    except ImportError:
        print("Matplotlib      : Not Found (Install via requirements.txt)")
        return False

    print("-" * 60)
    print("Environment setup verified successfully.")
    return True

if __name__ == "__main__":     # __name__ is a built-in variable that Python automatically assigns to every script/module when it runs.
    success = verify_environment()
    if not success:
        sys.exit(1)