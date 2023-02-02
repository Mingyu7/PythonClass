lines = ["we'll find a way we always have - Interstellar\n",
"I'll find tou and I'll kill you - Taken\n",
"I'll be back - Terminator 2\n"] 

with open('movie_quotes.txt','w') as file:
    file.writelines(lines) #for문과 같은 형식

    #for line in lines:
        #file.write(line)