import re

def parse_asn_file(content):
    result = {
        "supplier_id": None,
        "desadv_ref": None,
        "packaging_lines": []
    }
    
    if not content:
        return result
    
    lines = content.split('\n')
    current_packaging = None
    
    for line in lines:
        line = line.strip()
        
        # Parse header fields
        if line.startswith("SUPPLIER_ID:"):
            result["supplier_id"] = line.split(":", 1)[1].strip()
        elif line.startswith("DESADV_REF:"):
            result["desadv_ref"] = line.split(":", 1)[1].strip()
        
        # Parse packaging line headers
        elif line.startswith("[PACKAGING_LINE"):
            current_packaging = {}
            result["packaging_lines"].append(current_packaging)
        
        # Parse packaging line fields
        elif ":" in line and current_packaging is not None:
            key, value = line.split(":", 1)
            key = key.strip().lower()
            value = value.strip()
            
            # Handle quantity conversion with error handling
            if key == "qty":
                try:
                    current_packaging[key] = int(value)
                except ValueError:
                    current_packaging[key] = 0  # Default to 0 for invalid numbers
            else:
                current_packaging[key] = value
    
    return result

