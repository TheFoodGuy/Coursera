#making everything simple to import and what not

#PatternCount 
def PatternCount(text, Pattern): 
    count = []
    for i in range(len(text) - len(Pattern) + 1): #should go up to 2 
        if text[i:len(Pattern)+i] == Pattern:
            count.append(i) 
    return count

#FrequentWord
def FrequentWords(text, k) : 
    #text - > genome_string 
    #k - > genome_pattern value 
    genome_count = {}
    for i in range(len(text) - k + 1): # < - from the instruction here
        pattern = text[i:k+i] 
        if pattern in genome_count: 
            genome_count[pattern] += 1
        else: 
            genome_count[pattern] = 1 
        max_count = max(genome_count.values())
    
    #target = [] # it prints the sequences with the greatest values, should be an even number of sequences 
    for k in genome_count: 
        if genome_count[k] == max_count: 
            print(k)
            #target.append(k) #there's really no point in doing this tho
            
#PatternMatching 
def PatternMatching(text, Pattern): 
    #count = []
    for i in range(len(text) - len(Pattern) + 1): #should go up to 2 
        if text[i:len(Pattern)+i] == Pattern:
            print ' ', i, ' ' 
            #count.append(i) 
    #return count

#PatternToNumber 
def PatternToNumber(Pattern):
    if Pattern == '':
        return 0 
    nucleotide_to_number = {'A':0, 'C':1, 'G':2, 'T':3}
    last_value = Pattern[-1]
    rem_pat = Pattern[:len(Pattern)-1] #ATGCA | A 
    return 4 * PatternToNumber(rem_pat) + nucleotide_to_number[last_value]

#NumberToPattern 
def NumberToPattern(num_position, seq_length):
    nuc_conversion = {0:'A', 1:'C', 2:'G', 3:'T'}
    if seq_length == 0: 
        return None
    elif seq_length == 1: 
        return nuc_conversion[num_position%4]
        #return numToalp(num_position%4)  
    next_value = num_position // 4 #1359 
    remainder = nuc_conversion[num_position%4]
    #remainder = numToalp(num_position % 4) #R 1 -> C 
    return NumberToPattern(next_value, seq_length-1) + remainder

#new FrequentWords 
def FrequentWords(Text, k):
    FrequencyArray = [0 for i in range((4**k))] 

    for i in range(0, len(Text)-k+1):
        pattern = Text[i:k+i]
        j = PatternToNumber(pattern)
        #print pattern #confirmation that everything was being taken into account 
        FrequencyArray[j] = FrequencyArray[j] + 1
        
    return FrequencyArray

#new and improved Clump using frequentwords
def NumberToPattern(num_position, seq_length):
    nuc_conversion = {0:'A', 1:'C', 2:'G', 3:'T'}
    if seq_length == 0: 
        return None
    elif seq_length == 1: 
        return nuc_conversion[num_position%4]
    next_value = num_position // 4 #1359 
    remainder = nuc_conversion[num_position%4]
    return NumberToPattern(next_value, seq_length-1) + remainder

def FrequentWords(Text, k):
    FrequencyArray = [0 for i in range((4**k))] 

    for i in range(0, len(Text)-k+1):
        pattern = Text[i:k+i]
        j = PatternToNumber(pattern)
        #print pattern #confirmation that everything was being taken into account 
        FrequencyArray[j] = FrequencyArray[j] + 1
        
    return FrequencyArray

def find_clump(genome, k , L , t):
    FrequentPat = set()
    Clump = [0] * (4**k - 1) #seems really wasteful here 
    Text = genome[0:L]
    FrequencyArray = FrequentWords(Text, k)
    for i in range (4**k - 1):
        if FrequencyArray[i] >= t: 
            Clump[i] = 1
    for i in range(1, len(genome)-L):
        first_pattern = genome[i-1:i-1+k] #double check here | genome(i-1, k) 
        index = PatternToNumber(first_pattern)
        print index , len(FrequencyArray)
        print ("im here")
        FrequencyArray[index] = FrequencyArray[index] - 1
        last_pattern = genome[i+L-k: L+i] #genome(i + L - k, k)
        index = PatternToNumber(last_pattern)
        FrequencyArray[index] = FrequencyArray[index] + 1
        if FrequencyArray[index] >= t: 
            Clump[index] = 1 
    for i in range(4**k - 1): 
        if Clump[i] == 1: 
            Pattern = NumberToPattern(i, k)
            FrequentPat.add(Pattern)
    return FrequentPat

#slow clump with frequentwords 
def find_clump(genome, k, L, t):
    FrequentPat = set()
    Clump = [0] * (4**k - 1)
    for i in range(0, len(genome)-L):
        Text = genome[i:i+L]
        FrequencyArray = FrequentWords(Text, k)
        for index in range(0, 4**k - 1):
            if FrequencyArray[index] >= t:
                Clump[index] = 1 
    for i in range(0, 4**k - 1):
        if Clump[i] == 1: 
            Pattern = NumberToPattern(i,k)
            FrequentPat.add(Pattern)
    return sorted(FrequentPat)

#reverse complement 
def reverse_complement_problem(string):
    dictionary = {"A":"T", "T":"A", "C":"G", "G":"C"}
    output = [dictionary[x] for x in string[::-1]]
    return "".join(output)