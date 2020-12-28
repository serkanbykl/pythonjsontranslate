from googletrans import Translator

#Google Translator
translator = Translator()

#File open.
read=open("json.txt", "r")
write=open("new.txt", "a+")

#For in read file.
for j in read:
  
    #Split word.
    a=j.split("\n")
    
    #Not translate link.
    if (":" in a[0]) and ("http" not in a[0]):
      
      #Split of the split.
      b=a[0].split(":")
      
      #if b = { or [ or [{ (only).
      if (len(b[1]) > 3):
        
        #if b[1] = false or true or null and email address.
        if('"' in b[1]) and ("@" not in b[1]):
          
          #translate word.
          translation = translator.translate(str(b[1]), dest='tr')
          
          #old = new word
          b[1]=translation.text

        #display
        print(b[0] + ": " + b[1])
        
      #new line (new a)  
      text=str(b[0] + ": " +  b[1])
      write.write(text + "\n")
      
    else:
        write.write(a[0] +"\n")

#File close.
write.close()
read.close()
