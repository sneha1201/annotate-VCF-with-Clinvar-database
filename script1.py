import subprocess
import pandas as pd

def vcf_reader(srr_vcf_path, clinvar_vcf_path):
    clinvar_data = {}

    # Read clinvar.vcf and store relevant data in a dictionary
    with open(clinvar_vcf_path, 'r') as clinvar_file:
        for line in clinvar_file:
            if line.startswith('#'):
                continue  # Skip header lines
            parts = line.strip().split('\t')
            chr_pos = (parts[0], parts[1])  # (chr, pos) as key
            clndn = None
            # Extract CLNDN field from the INFO column (8th column)
            for info in parts[7].split(';'):
                if info.startswith('CLNDN='):
                    clndn = info.split('=')[1] # Get the CLNDN value
                    break
            if clndn:
                clinvar_data[chr_pos] = clndn  # Store in dictionary

    # Read SRR9050857.vcf and annotate with CLNDN from clinvar.vcf
    output_vcf_path = 'SRR9050857_annot.vcf'
    with open(srr_vcf_path, 'r') as srr_file, open(output_vcf_path, 'w') as output_file:
        for line in srr_file:
            if line.startswith('#'):
                output_file.write(line)  # Write header lines as is
                continue
            parts = line.strip().split('\t')
            chr_pos = (parts[0], parts[1])  # (chr, pos) as key
            if chr_pos in clinvar_data:
                parts[7] += f";CLNDN={clinvar_data[chr_pos]}"  # Annotate with CLNDN
            output_file.write('\t'.join(parts) + '\n')  # Write modified line

    return output_vcf_path  # Return path of the annotated VCF file

def vcf_parser(annot_vcf_path):
    clndn_count = {}

    # Parse annotated VCF file and count CLNDN occurrences
    with open(annot_vcf_path, 'r') as annot_file:
        for line in annot_file:
            if line.startswith('#'):
                continue  # Skip header lines
            parts = line.strip().split('\t')
            info_field = parts[7]
            if 'CLNDN=' in info_field:
                clndn = info_field.split('CLNDN=')[1].split(';')[0]  # Extract CLNDN value
                clndn_count[clndn] = clndn_count.get(clndn, 0) + 1  # Count occurrences

    # Output the counts to a table
    output_table_path = 'clndn_counts.tsv'
    with open(output_table_path, 'w') as table_file:
        table_file.write('CLNDN\tCount\n')  # Header
        for clndn, count in clndn_count.items():
            table_file.write(f'{clndn}\t{count}\n')  # Write each CLNDN and its count

    return output_table_path  # Return path of the output table

def visualizer(table_path):
    # Call script2.py with the table path as an argument
    subprocess.run(['python3', 'script2.py', table_path])

if __name__ == "__main__":
    # paths to the VCF files
    srr_vcf_path = '/Users/snehagoel/Downloads/SRR9050857.vcf'
    clinvar_vcf_path = '/Users/snehagoel/Downloads/clinvar.vcf'  

    annotated_vcf_path = vcf_reader(srr_vcf_path, clinvar_vcf_path)  # Annotate VCF
    table_path = vcf_parser(annotated_vcf_path)  # Generate CLNDN count table
    visualizer(table_path)  # Visualize the results
