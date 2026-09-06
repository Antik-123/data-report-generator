import csv
from datetime import datetime

def process_logs(input_file, output_file):
    total_logs = 0
    resolved_count = 0
    categories = {}

    
    with open(input_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_logs += 1
            
            # Check if status is resolved
            if row['status'].strip().lower() == 'resolved':
                resolved_count += 1
            
            # Count entries per category
            cat = row['category']
            categories[cat] = categories.get(cat, 0) + 1


    resolution_rate = (resolved_count / total_logs * 100) if total_logs > 0 else 0

  
    with open(output_file, mode='w') as report:
        report.write("=== DAILY OPERATIONS SUMMARY REPORT ===\n")
        report.write(f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.write(f"Total Logs Processed: {total_logs}\n")
        report.write(f"Resolved Items: {resolved_count} ({resolution_rate:.1f}%)\n\n")
        report.write("Category Breakdown:\n")
        for cat, count in categories.items():
            report.write(f" - {cat}: {count}\n")

    print(f"Process complete! Output saved to: {output_file}")

if __name__ == "__main__":
    process_logs('logs.csv', 'daily_report.txt')