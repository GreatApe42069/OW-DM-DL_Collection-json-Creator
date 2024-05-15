import json
import os

def detect_input_format(input_data):
    if isinstance(input_data, list) and all("id" in item and "meta" in item for item in input_data):
        return "format1"
    elif isinstance(input_data, dict) and "body" in input_data and isinstance(input_data["body"], list):
        return "format3"
    else:
        return "format2"

def convert_to_format1(input_data):
    output_data = []
    for item in input_data:
        output_item = {
            "inscriptionId": item["id"],
            "name": item["meta"]["name"],
            "attributes": {}
        }
        for attr in item["meta"]["attributes"]:
            output_item["attributes"][attr["trait_type"]] = attr["value"]
        output_data.append(output_item)
    return output_data

def convert_to_format3(input_data):
    output_data = {
        "body": []
    }
    if isinstance(input_data, list):
        for item in input_data:
            output_item = {
                "inscriptionId": item["id"],
                "name": item["meta"]["name"],
                "collectionSymbol": "collection_name",
                "metadata": {}
            }
            for attr in item["meta"]["attributes"]:
                output_item["metadata"][attr["trait_type"]] = attr["value"]
            output_data["body"].append(output_item)
    elif isinstance(input_data, dict) and "body" in input_data:
        for item in input_data["body"]:
            output_item = {
                "inscriptionId": item["inscriptionId"],
                "name": item["name"],
                "collectionSymbol": "collection_name",
                "metadata": {}
            }
            for attr in item["metadata"]:
                output_item["metadata"][attr["trait_type"]] = attr["value"]
            output_data["body"].append(output_item)
    return output_data

def convert_json(input_file):
    # Read input JSON from file
    with open(input_file, 'r') as f:
        input_data = json.load(f)

    # Detect the format of the input JSON
    input_format = detect_input_format(input_data)
    print(f"Detected input format: {input_format}")

    # Convert input format to output formats
    if input_format == "format1":
        # Convert to output format 1 (outputDM.json)
        output_data_1 = convert_to_format1(input_data)
        output_json_1 = json.dumps(output_data_1, indent=4)
        output_file_1 = os.path.join(os.path.dirname(input_file), 'outputDM.json')
        with open(output_file_1, "w") as outfile:
            outfile.write(output_json_1)
        print(f"Output JSON saved to '{output_file_1}'")

        # Also generate outputOW.json
        output_json_2 = json.dumps(input_data, indent=4)
        output_file_2 = os.path.join(os.path.dirname(input_file), 'outputOW.json')
        with open(output_file_2, "w") as outfile:
            outfile.write(output_json_2)
        print(f"Output JSON saved to '{output_file_2}'")

        # Also generate outputDL.json
        output_data_3 = convert_to_format3(input_data)
        output_json_3 = json.dumps(output_data_3, indent=4)
        output_file_3 = os.path.join(os.path.dirname(input_file), 'outputDL.json')
        with open(output_file_3, "w") as outfile:
            outfile.write(output_json_3)
        print(f"Output JSON saved to '{output_file_3}'")

    elif input_format == "format3":
        # Convert to output format 3 (outputDL.json)
        output_data_3 = convert_to_format3(input_data)
        output_json_3 = json.dumps(output_data_3, indent=4)
        output_file_3 = os.path.join(os.path.dirname(input_file), 'outputDL.json')
        with open(output_file_3, "w") as outfile:
            outfile.write(output_json_3)
        print(f"Output JSON saved to '{output_file_3}'")

        # Also generate outputDM.json
        output_data_1 = convert_to_format1(input_data["body"])
        output_json_1 = json.dumps(output_data_1, indent=4)
        output_file_1 = os.path.join(os.path.dirname(input_file), 'outputDM.json')
        with open(output_file_1, "w") as outfile:
            outfile.write(output_json_1)
        print(f"Output JSON saved to '{output_file_1}'")

        # Also generate outputOW.json
        output_json_2 = json.dumps(input_data, indent=4)
        output_file_2 = os.path.join(os.path.dirname(input_file), 'outputOW.json')
        with open(output_file_2, "w") as outfile:
            outfile.write(output_json_2)
        print(f"Output JSON saved to '{output_file_2}'")

    else:
        # Convert to output format 2 (outputOW.json)
        output_json_2 = json.dumps(input_data, indent=4)
        output_file_2 = os.path.join(os.path.dirname(input_file), 'outputOW.json')
        with open(output_file_2, "w") as outfile:
            outfile.write(output_json_2)
        print(f"Output JSON saved to '{output_file_2}'")

        # Also generate outputDM.json
        output_data_1 = convert_to_format1(input_data)
        output_json_1 = json.dumps(output_data_1, indent=4)
        output_file_1 = os.path.join(os.path.dirname(input_file), 'outputDM.json')
        with open(output_file_1, "w") as outfile:
            outfile.write(output_json_1)
        print(f"Output JSON saved to '{output_file_1}'")

        # Also generate outputDL.json
        output_data_3 = convert_to_format3({"body": input_data})
        output_json_3 = json.dumps(output_data_3, indent=4)
        output_file_3 = os.path.join(os.path.dirname(input_file), 'outputDL.json')
        with open(output_file_3, "w") as outfile:
            outfile.write(output_json_3)
        print(f"Output JSON saved to '{output_file_3}'")

if __name__ == "__main__":
    # Get the path to the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set the input file path
    input_file = os.path.join(script_dir, "input.json")
    
    # Convert the JSON and save the output
    convert_json(input_file)
