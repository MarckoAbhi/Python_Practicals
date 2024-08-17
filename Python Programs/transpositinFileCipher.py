import time, os, sys, transpositionEncrypt, transpositionDecryption

def main():
    inputFilename = 'frankenstein.txt'
    
    outputFilename = 'frankestein.encrypted.txt'
    
    myKey = 10
    myMode= 'encrypt'
    
    if not os.path.exists(inputFilename):
        print('The file %s does not exit. Quitting...' %(inputFilename))
        sys.exit()
        
    if os.path.exists(outputFilename):
        
        print('This will overwrite the file %s. (c)ontinue or (Q)uit?' %(outputFilename))
        response = input('> ')
        if not response.lower().stratwith('c'):
            sys.exit()
            
        fileObj = open(inputFilename)
        content = fileObj.read()
        fileObj.close()
        
        print('%sing...' % (myMode.title()))
        startTime = time.time()
        
        if myMode =='encrypt':
            translated = transpositionEncrypt.encryptMessage(myKey, content)
            
        elif myMode=='decrypt':
            translated= transpositionDecryption.decryptMessage(myKey, content)
            
        totalTime = round(time.time() - startTime, 2)
        print('%sion time: %s seconds' % (myMode.title(), totalTime))
        
        outputFileObj = open(outputFilename, 'w')
        outputFileObj.write(translated)
        outputFileObj.close()
        
        print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
        
        print('%sed file is %s.' %(myMode.title(), outputFilename))
            
if __name__== '__main__':
    main()
    