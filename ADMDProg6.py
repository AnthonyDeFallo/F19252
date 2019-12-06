"""Anthony DeFallo"""

from ADMDMachine import ADMDMachine

def start_transitions(txt):
    splitted_txt = txt.split(None,1)
    digit, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if digit == "0":
        newState = "a_state"
    elif digit == "1":
        newState = "neg_state"
    else:
        newState = "error_state"
    return (newState, txt)

def a_state(txt):
    splitted_txt = txt.split(None,1)
    digit, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if digit == "0":
        newState = "b_state"
    elif digit == "1":
        newState = "neg_state"
    else:
        newState = "error_state"
    return (newState, txt)

def b_state(txt):
    splitted_txt = txt.split(None,1)
    digit, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if digit == "0":
        newState = "neg_state"
    elif digit == "1":
        newState = "rep_state"
    else:
        newState = "error_state"
    return (newState, txt)

def rep_state(txt):
    splitted_txt = txt.split(None,1)
    digit, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if digit == "0":
        newState = "a_state"
    elif digit == "1":
        newState = "neg_state"
    elif not digit:
        newState = "pos_state"
    else:
        newState = "error_state"
    return (newState, txt)

def neg_state(txt):
    print("Hallo")
    return ("neg_state", "")

if __name__== "__main__":
    m = ADMDMachine()
    m.add_state("Start", start_transitions)
    m.add_state("b_state", b_state)
    m.add_state("a_state", a_state)
    m.add_state("rep_state", rep_state)
    m.add_state("neg_state", None, end_state=1)
    m.add_state("pos_state", None, end_state=1)
    m.add_state("error_state", None, end_state=1)
    m.set_start("Start")
    m.run("0 1 0")
    m.run("0 0 1")
    m.run("1 0 0 1")
    m.run("0 0 1 0 0 1")
    m.run("0 0 1 0 0 1 0 0 1 0 0 1")
    m.run("0 0 1 0 0 1 0 0 1 0 1 0")
    
    """
    Pseudocode
    
    Accept input of the string
    Check state of the first digit
        If 0, move to A state
        If 1, not a pattern
    Check state of second digit
        If 0, move to B state
        If 1, not a pattern
    Check state of third digit
        If 0, not a pattern
        If 1, move to repetition state
        
    End program when found to not be a pattern or out of digits to process and output given state   
    
    """
    
    
    """
    UML
    
    States
    + Start
    + b_state
    + a_state
    + rep_state
    + neg_state
    + pos_state
    + error_state

        
    ConcreteStates
    + 0 1 0
    + 0 0 1
    + 1 0 0 1
    + 0 0 1 0 0 1
    + 0 0 1 0 0 1 0 0 1 0 0 1
    + 0 0 1 0 0 1 0 0 1 0 1 0
    
    
    """