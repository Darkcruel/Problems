# link : https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

def designerPdfViewer(h, word):
    # Write your code here
    height = 0
    
    for letter in word:
        height = max(height, h[ord(letter)-97])
    return height * len(word)
