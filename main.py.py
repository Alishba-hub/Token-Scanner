import re 
import tkinter as tk 
from tkinter import scrolledtext

count2 = 0
language = False

token_regex = r'\b(if|else|while|for|cout|cin|int|main|float|char|void|return|auto|break|case|const|continue|default|do|double|enum|extern|goto|long|register|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|volatile)\b|\b[a-zA-Z_][a-zA-Z0-9_]*\b|\d+|\S'#keywords + literal+identifiers(complete regular expression)
token_java_regex = r'\b(if|else|while|for|class|public|private|static|void|return|int|float|char|String|abstract|assert|boolean|break|byte|case|catch|const|continue|default|do|double|enum|extends|final|finally|goto|implements|import|instanceof|interface|native|new|package|protected|short|static|strictfp|super|switch|synchronized|this|throw|throws|transient|try|volatile|while|true|false|null)\b|\b[a-zA-Z_][a-zA-Z0-9_]*\b|\b\d+\b|\b[{}();,]\b|\S'
token_php_regex = r'\b(if|else|while|for|class|public|private|static|function|return|int|float|string|abstract|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|finally|for|foreach|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|namespace|new|or|print|protected|require|require_once|switch|throw|trait|try|unset|use|var|while|xor|yield|yield from|halt_compiler)\b|\b[a-zA-Z][a-zA-Z0-9]*\b|\b\d+\b|\b[{}();,]\b|\S'
token_python_regex = r'\b(if|else|while|for|def|return|print|class|import|from|as|True|False|None|and|assert|break|continue|del|elif|except|finally|from|global|if|in|is|lambda|nonlocal|not|or|pass|raise|try|while|with|yield)\b|\b[a-zA-Z_][a-zA-Z0-9_]*\b|\b\d+\b|\b[{}();,]\b|\S'

def count_token():
    global count2
    count = 0
    for _ in re.finditer(token_regex, input_str):
        count += 1
    count2 = count

def python_token():
    global count2, language
    val = 0
    for token in re.finditer(token_python_regex, input_str):
        token_str = token.group()
        next_token = token.end()
        if next_token < len(input_str):
            token2 = input_str[next_token]
        else:
            token2 = ''
        if re.match(r'\b(if|else|while|for|def|return|print|class|import|from|as|True|False|None|and|assert|break|continue|del|elif|except|finally|from|global|if|in|is|lambda|nonlocal|not|or|pass|raise|try|while|with|yield)\b', token_str):
            output_text.insert(tk.END, f"Python Keyword: {token_str}\n")
            val += 1
        elif re.match(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', token_str) and (token2 == '=' or token2 == '==') and not re.match(r'\b(if|else|while|for|cout|cin|int|main|float|char|void|return|auto|break|case|const|continue|default|do|_halt_compiler|abstract|and|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|else|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|finally|fn|for|foreach|function|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|match|namespace|new|or|print|private|protected|public|readonly|require|require_once|return|static|switch|throw|trait|try|unset|use|var|while|xor|yield|yield from|do|double|enum|extern|goto|long|register|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|volatile|if|else|while|for|class|public|private|static|void|return|int|float|char|String|abstract|assert|boolean|break|byte|case|catch|const|continue|default|do|double|enum|extends|final|finally|goto|implements|import|instanceof|interface|native|new|package|protected|short|static|strictfp|super|switch|synchronized|this|throw|throws|transient|try|volatile|while|true|false|null|if|else|while|for|class|public|private|static|function|return|int|float|string|abstract|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|finally|for|foreach|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|namespace|new|or|print|protected|require|require_once|switch|throw|trait|try|unset|use|var|while|xor|yield|yield from|_halt_compiler|if|else|while|for|def|return|print|class|import|from|as|True|False|None|and|assert|break|continue|del|elif|except|finally|from|global|if|in|is|lambda|nonlocal|not|or|pass|raise|try|while|with|yield)\b', token_str):
            output_text.insert(tk.END, f"Python Identifier: {token_str}\n")
            val += 1
        elif re.match(r'\d+', token_str) or (re.match(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', token_str) and not re.match(#d+ numeric value
                r'\b(if|else|while|for|cout|cin|int|main|float|char|void|return|auto|break|case|const|continue|default|do|_halt_compiler|abstract|and|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|else|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|finally|fn|for|foreach|function|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|match|namespace|new|or|print|private|protected|public|readonly|require|require_once|return|static|switch|throw|trait|try|unset|use|var|while|xor|yield|yield from|do|double|enum|extern|goto|long|register|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|volatile|if|else|while|for|class|public|private|static|void|return|int|float|char|String|abstract|assert|boolean|break|byte|case|catch|const|continue|default|do|double|enum|extends|final|finally|goto|implements|import|instanceof|interface|native|new|package|protected|short|static|strictfp|super|switch|synchronized|this|throw|throws|transient|try|volatile|while|true|false|null|if|else|while|for|class|public|private|static|function|return|int|float|string|abstract|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|finally|for|foreach|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|namespace|new|or|print|protected|require|require_once|switch|throw|trait|try|unset|use|var|while|xor|yield|yield from|_halt_compiler|if|else|while|for|def|return|print|class|import|from|as|True|False|None|and|assert|break|continue|del|elif|except|finally|from|global|if|in|is|lambda|nonlocal|not|or|pass|raise|try|while|with|yield|=|==)\b', token_str)):
            output_text.insert(tk.END, f"Python Literal: {token_str}\n")
            val += 1
        elif token_str in "!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~":#symbol
            output_text.insert(tk.END, f"Python Symbol: {token_str}\n")
            val += 1
        else:
            output_text.insert(tk.END, f"Not a part a Python Language: {token_str}\n")
    if val == count2:
        output_text.insert(tk.END, "THIS INPUT BELONGS TO PYTHON LANGUAGE\n")
        language = True

def c_token():
    global count2, language
    val = 0
    for token in re.finditer(token_regex, input_str):
        token_str = token.group()
        next_token = token.end()
        if next_token < len(input_str):
            token2 = input_str[next_token]
        else:
            token2 = ''
        if re.match(r'\b(if|else|while|for|cout|cin|auto|break|case|continue|default|do|double|enum|extern|goto|long|register|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|volatile)\b', token_str):
            output_text.insert(tk.END, f"C/C++ Keyword: {token_str}\n")
            val += 1
        elif re.match(r'\b(int|float|double|char|void|string)\b', token_str):
            output_text.insert(tk.END, f"C/C++ Data Type: {token_str}\n")
            val += 1
        elif re.match(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', token_str) and (token2 == '=' or token2 == '=='):
            output_text.insert(tk.END, f"C/C++ Identifier: {token_str}\n")
            val += 1
        elif re.match(r'\d+', token_str) or (re.match(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', token_str) and not re.match(
                r'\b(if|else|while|for|cout|cin|auto|break|case|const|continue|default|do|_halt_compiler|abstract|and|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|else|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|finally|fn|for|foreach|function|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|match|namespace|new|or|print|private|protected|public|readonly|require|require_once|return|static|switch|throw|trait|try|unset|use|var|while|xor|yield|yield from|do|double|enum|extern|goto|long|register|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|volatile|if|else|while|for|class|public|private|static|void|return|int|float|char|String|abstract|assert|boolean|break|byte|case|catch|const|continue|declare|default|do|double|enum|extends|final|finally|goto|implements|import|instanceof|interface|native|new|package|protected|short|static|strictfp|super|switch|synchronized|this|throw|throws|transient|try|volatile|while|true|false|null|if|else|while|for|class|public|private|static|function|return|int|float|string|abstract|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|finally|for|foreach|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|namespace|new|or|print|protected|require|require_once|switch|throw|trait|try|unset|use|var|while|xor|yield|yield from|_halt_compiler|if|else|while|for|def|return|print|class|import|from|as|True|False|None|and|assert|break|continue|del|elif|except|finally|from|global|if|in|is|lambda|nonlocal|not|or|pass|raise|try|while|with|yield)\b',
                token_str)):
            output_text.insert(tk.END, f"C/C++ Literal: {token_str}\n")
            val += 1
        elif token_str in "!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~":#symbol
            output_text.insert(tk.END, f"C/C++ Symbol: {token_str}\n")
            val += 1
        else:
            output_text.insert(tk.END, f"Not a part a C/C++ Language: {token_str}\n")
    if val == count2:
        output_text.insert(tk.END, "THIS INPUT BELONGS TO C/C++ LANGUAGE\n")
        language = True

def java_token():
    global count2, language
    val = 0
    for token in re.finditer(token_java_regex, input_str):
        token_str = token.group()
        next_token = token.end()
        if next_token < len(input_str):
            token2 = input_str[next_token]
        else:
            token2 = ''
        if re.match(r'\b(if|else|while|for|class|public|private|static|void|return|int|float|char|String|abstract|assert|boolean|break|byte|case|catch|const|continue|default|do|double|enum|extends|final|finally|goto|implements|import|instanceof|interface|native|new|package|protected|short|static|strictfp|super|switch|synchronized|this|throw|throws|transient|try|volatile|while|true|false|null)\b',
                    token_str):
            output_text.insert(tk.END, f"Java Keyword: {token_str}\n")
            val += 1
        elif re.match(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', token_str) and (token2 == '=' or token2 == '=='):
            output_text.insert(tk.END, f"Java Identifier: {token_str}\n")
            val += 1
        elif re.match(r'\d+', token_str) or (re.match(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', token_str) and not re.match(
                r'\b(if|else|while|for|cout|cin|int|main|float|char|void|return|auto|break|case|const|continue|default|do|_halt_compiler|abstract|and|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|else|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|finally|fn|for|foreach|function|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|match|namespace|new|or|print|private|protected|public|readonly|require|require_once|return|static|switch|throw|trait|try|unset|use|var|while|xor|yield|yield from|double|enum|extern|goto|long|register|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|volatile|if|else|while|for|class|public|private|static|void|return|int|float|char|String|abstract|assert|boolean|break|byte|case|catch|const|continue|declare|default|do|double|enum|extends|final|finally|goto|implements|import|instanceof|interface|native|new|package|protected|short|static|strictfp|super|switch|synchronized|this|throw|throws|transient|try|volatile|while|true|false|null|if|else|while|for|class|public|private|static|function|return|int|float|string|abstract|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|finally|for|foreach|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|namespace|new|or|print|protected|require|require_once|switch|throw|trait|try|unset|use|var|while|xor|yield|yield from|_halt_compiler|if|else|while|for|def|return|print|class|import|from|as|True|False|None|and|assert|break|continue|del|elif|except|finally|from|global|if|in|is|lambda|nonlocal|not|or|pass|raise|try|while|with|yield)\b',
                token_str)):
            output_text.insert(tk.END, f"Java Literal: {token_str}\n")
            val += 1
        elif token_str in "!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~":#symbol
            output_text.insert(tk.END, f"Java Symbol: {token_str}\n")
            val += 1
        else:
            output_text.insert(tk.END, f"Not a part a Java Language: {token_str}\n")
    if val == count2:
        output_text.insert(tk.END, "THIS INPUT BELONGS TO JAVA LANGUAGE\n")
        language = True

def php_token():
    global count2, language, input_str, output_text
    val = 0
    check = 0
    for token in re.finditer(token_php_regex, input_str):
        if check == 1:
            check = 0
            continue
        token_str = token.group()
        next_token = token.end()
        if next_token < len(input_str):
            token2 = input_str[next_token]
        else:
            token2 = ''
        if re.match(r'\b(__halt_compiler|abstract|and|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|else|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|finally|fn|for|foreach|function|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|match|namespace|new|or|print|private|protected|public|readonly|require|require_once|return|static|switch|throw|trait|try|unset|use|while|xor|yield|yield from)\b', token_str):
            output_text.insert(tk.END, f"PHP Keyword: {token_str}\n")
            val += 1
        elif token_str == '$':
            output_text.insert(tk.END, f"PHP Symbol: {token_str}\n")
            if next_token < len(input_str):
                token2 = re.match(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', input_str[next_token:])
                if token2:
                    token2_str = token2.group()
                    output_text.insert(tk.END, f"PHP Identifier: {token2_str}\n")
                    next_token += len(token2_str)
                    val += 2
                    check = 1
        elif re.match(r'\d+', token_str) or (re.match(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', token_str) and not re.match(
                r'\b(if|else|while|for|cout|cin|int|main|float|char|void|return|auto|break|case|const|continue|default|_halt_compiler|abstract|and|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|else|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|finally|fn|for|foreach|function|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|match|namespace|new|or|print|private|protected|public|readonly|require|require_once|return|static|switch|throw|trait|try|unset|use|while|xor|yield|yield from|do|double|enum|extern|goto|long|register|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|volatile|if|else|while|for|class|public|private|static|void|return|int|float|char|String|abstract|assert|boolean|break|byte|case|catch|const|continue|declare|default|do|double|enum|extends|final|finally|goto|implements|import|instanceof|interface|native|new|package|protected|short|static|strictfp|super|switch|synchronized|this|throw|throws|transient|try|volatile|while|true|false|null|if|else|while|for|class|public|private|static|function|return|int|float|string|abstract|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|finally|for|foreach|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|namespace|new|or|print|protected|require|require_once|switch|throw|trait|try|unset|use|var|while|xor|yield|yield from|_halt_compiler|if|else|while|for|def|return|print|class|import|from|as|True|False|None|and|assert|break|continue|del|elif|except|finally|from|global|if|in|is|lambda|nonlocal|not|or|pass|raise|try|while|with|yield)\b',
                token_str)):
            output_text.insert(tk.END, f"PHP Literal: {token_str}\n")
            val += 1
        elif token_str in "!\"$#%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            output_text.insert(tk.END, f"PHP Symbol: {token_str}\n")
            val += 1
        else:
            output_text.insert(tk.END, f"Not a part of PHP Language: {token_str}\n")
    if val == count2:
        output_text.insert(tk.END, "THIS INPUT BELONGS TO PHP LANGUAGE\n")
        language = True

def get_input():
    global input_str, count2, language
    input_str = input_text.get("1.0", tk.END)
    count_token()
    output_text.delete("1.0",tk.END)
    python_token()
    if not language:
        c_token()
        if not language:
            java_token()
            if not language:
                php_token()

def clear_output():
    output_text.delete("1.0", tk.END)

def clear_input():
    input_text.delete("1.0", tk.END)

window = tk.Tk()
window.title("Langauge Detector")
window.geometry("800x600")

input_text = scrolledtext.ScrolledText(window, wrap = tk.WORD, width = 40, height= 10)
input_text.place(x=50,y=50)

output_text = scrolledtext.ScrolledText(window, wrap = tk.WORD, width = 40, height= 10)
output_text.place(x=450,y=50)

analyze_button = tk.Button(window, text = "Analyze", command = get_input)
analyze_button.place(x=100, y=200)

clear_input_button = tk.Button(window, text = "Clear Input", command= clear_input)
clear_input_button.place(x=200,y=200)

clear_input_button = tk.Button(window, text = "Clear Output", command= clear_output)
clear_input_button.place(x=300,y=200)

window.mainloop()