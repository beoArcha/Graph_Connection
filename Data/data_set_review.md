1. WineDataSet:
    - class (class): 
        - from 1 to 3
    - index: 0
    - attributes
        0) class
        1) Alcohol
        2) Malic acid
        3) Ash
        4) Alcalinity of ash
        5) Magnesium
        6) Total phenols
        7) Flavanoids
        8) Nonflavanoid phenols
        9) Proanthocyanins
        10) Color intensity
        11) Hue
        12) OD280/OD315 of diluted wines
        13) Proline
    - number of attributes: 14
    - number of records: 178   
    - link: https://archive.ics.uci.edu/ml/datasets/Wine   
2. Contraceptive
    - number of attributes: 9
    - number of records: 1473 
	- no. of class: 3	
    - link: http://archive.ics.uci.edu/ml/datasets/Contraceptive+Method+Choice
3. Health:                
4. Iris:
    - class (class): 
        - 1 - Iris-setosa
        - 2 - Iris-versicolor
        - 3 - Iris-virginica
    - index: False
    - number of attributes: 5
    - number of records: 150   
    - link: https://archive.ics.uci.edu/ml/datasets/iris/
5. Heart swiss:
    - link: https://archive.ics.uci.edu/ml/datasets/Heart+Disease
    - Attribute:
      -- 1. #3  (age)       
      -- 2. #4  (sex)       
      -- 3. #9  (cp)        
      -- 4. #10 (trestbps)  
      -- 5. #12 (chol)      
      -- 6. #16 (fbs)       
      -- 7. #19 (restecg)   
      -- 8. #32 (thalach)   
      -- 9. #38 (exang)     
      -- 10. #40 (oldpeak)   
      -- 11. #41 (slope)     
      -- 12. #44 (ca)        
      -- 13. #51 (thal)      
      -- 14. #58 (num)       (the predicted attribute)
	- class (num)  
	- index: False
    - number of attributes: 13
    - number of records: 123
6. Wine quality:
    - link: https://archive.ics.uci.edu/ml/datasets/Wine+Quality
	- class (quality):
		- from 0 to 10
	- index: False
    - number of attributes: 12
    - number of records: 1599 	
7. Yeast: 
    - class (class):
        - 1 - CYT
        - 2 - NUC
        - 3 - MIT 
        - 4 - ME3 
        - 5 - ME2 
        - 6 - ME1 
        - 7 - EXC 
        - 8 - VAC 
        - 9 - POX 
        - 10 - ERL 
    - link: https://archive.ics.uci.edu/ml/datasets/Yeast
    - Attribute:
        1.  Sequence Name: Accession number for the SWISS-PROT database
        2.  mcg: McGeoch's method for signal sequence recognition.
        3.  gvh: von Heijne's method for signal sequence recognition.
        4.  alm: Score of the ALOM membrane spanning region prediction program.
        5.  mit: Score of discriminant analysis of the amino acid content of
            the N-terminal region (20 residues long) of mitochondrial and 
               non-mitochondrial proteins.
        6.  erl: Presence of "HDEL" substring (thought to act as a signal for
           retention in the endoplasmic reticulum lumen). Binary attribute.
        7.  pox: Peroxisomal targeting signal in the C-terminus.
        8.  vac: Score of discriminant analysis of the amino acid content of
               vacuolar and extracellular proteins.
        9.  nuc: Score of discriminant analysis of nuclear localization signals
        of nuclear and non-nuclear proteins. 
        10. class
    - index: name
    - number of attributes: 9
    - number of records: 1484		
8. Magic :
    - link: https://archive.ics.uci.edu/ml/datasets/MAGIC+Gamma+Telescope
    - class (class:
        - 1 - gamma (signal)
        - 2 - hadron (background)     
    - index: False
    - number of attributes: 11
    - number of records: 19020		
9. ILPD
    - name: Indian Liver Patient Dataset (ILPD)
    - link: https://archive.ics.uci.edu/ml/datasets/ILPD+%28Indian+Liver+Patient+Dataset%29
    - Attribute:
        1. Age Age of the patient
        2. Gender Gender of the patient Male-0 Female-1
        3. TB Total Bilirubin
        4. DB Direct Bilirubin
        5. Alkphos Alkaline Phosphotase
        6. Sgpt Alamine Aminotransferase
        7. Sgot Aspartate Aminotransferase
        8. TP Total Protiens
        9. ALB Albumin
        10. A/G Ratio Albumin and Globulin Ratio
        11. Selector field used to split the data into two sets (labeled by the experts)  
	- class	(Selector)
    - index: False
    - number of attributes: 11
    - number of records: 583		
10. Cryotherapy:
    - link: https://archive.ics.uci.edu/ml/datasets/Cryotherapy+Dataset+
	- class (Result_of_Treatment)
		- 0 - failure
		- 1 - success
    - index: False
    - number of attributes: 7
    - number of records: 90 	
11. Knowledge:  
    - link: https://archive.ics.uci.edu/ml/datasets/User+Knowledge+Modeling
    - class (UNS):
        - 1 - very low
        - 2 - low
        - 3 - medium
        - 4 - high
    - index: False
    - number of attributes: 6
    - number of records: 258		
12. Breast_tissue:
    - link: https://archive.ics.uci.edu/ml/datasets/Breast+Tissue
    - class (Class):
        - 1 - car
        - 2 - fad
        - 3 - mas
        - 4 - gla
        - 5 - con
        - 6 - adi
    - index: Case
    - number of attributes: 10
    - number of records: 106		
13. Blood:
    - link: https://archive.ics.uci.edu/ml/datasets/Blood+Transfusion+Service+Center
    - class (class)
        - whether he/she donated blood in March 2007?
        - 1 - True
        - 0 - False
    - index: False
    - number of attributes: 5
    - number of records: 748		
14. Mammographic:
    - link: https://archive.ics.uci.edu/ml/datasets/Mammographic+Mass
	- class(Severity):
	
    - index:  False
    - number of attributes: 6
    - number of records: 961	
15. Voting:
    - link: https://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records
    - class (class):
        - republican - 0
        - democrat - 1
    votes:
        - 1 - yea
        - -1 - nae  
    Attributes: different votes
	- index: False
    - number of attributes: 16
    - number of records: 435 
      