# annotate-VCF-with-Clinvar-database
Python script to annotate raw vcf with Clinvar database and create a barplot
Requirements : Python is installed in the root .

Data Require
    •  Clinvar.vcf file (clinvar database file )
Download from : https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.vcf.gz
    • SRR9050857.vcf (file which need to be annotated )

Usage : 

    • In script1.py give the absolute path of clinvar and the file which need to be annotated 
 
    srr_vcf_path = '/Users/snehagoel/Downloads/SRR9050857.vcf’
    clinvar_vcf_path = '/Users/snehagoel/Downloads/clinvar.vcf'  

    • Both scrip1.py and script2.py should be in same directory 
    • Script will make output in the same directory as of vcf files 

RUN SCRIPT : python3 scrip1.py 

(give the absolute path of the script )

    
Output : 
clndn_counts.tsv : contains the CLNDN and counts as a row and has the count of disease coming in the VCF file .
clndn_frequency_chart.png : Barplot of top 6 fields for the sheet .
SRR9050857_annot.vcf : Annotated vcf , in INFO field CLNDN information is added . 
    

