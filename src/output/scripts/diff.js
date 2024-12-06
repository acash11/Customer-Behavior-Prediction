function compareAntecedentsConsequents() {
    var sheet1 = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Sheet4');
    var sheet2 = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Sheet5');
    var sheet3 = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Sheet6');
    
    // Clear any existing data in Sheet3 before writing new results
    sheet3.clear();
    
    var data1 = sheet1.getDataRange().getValues();  // Get data from Sheet1
    var data2 = sheet2.getDataRange().getValues();  // Get data from Sheet2
    
    var differences = [];
    
    // Compare each rule in Sheet1 against Sheet2
    for (var i = 0; i < data1.length; i++) {
      var antecedent1 = data1[i][0]; // Assuming antecedent is in column A
      var consequent1 = data1[i][1]; // Assuming consequent is in column B
      
      var foundInSheet2 = false;
      
      // Check if antecedent and consequent in Sheet1 exist in Sheet2
      for (var j = 0; j < data2.length; j++) {
        var antecedent2 = data2[j][0]; // Antecedent in Sheet2
        var consequent2 = data2[j][1]; // Consequent in Sheet2
        
        if (antecedent1 === antecedent2 && consequent1 === consequent2) {
          foundInSheet2 = true;
          break;
        }
      }
      
      // If no match found, record the rule as "Not Found"
      if (!foundInSheet2) {
        differences.push(['Rule not found in Sheet2: ' + antecedent1 + ' => ' + consequent1]);
      }
    }
    
    // Now check for rules in Sheet2 not found in Sheet1
    for (var i = 0; i < data2.length; i++) {
      var antecedent2 = data2[i][0]; // Antecedent in Sheet2
      var consequent2 = data2[i][1]; // Consequent in Sheet2
      
      var foundInSheet1 = false;
      
      for (var j = 0; j < data1.length; j++) {
        var antecedent1 = data1[j][0]; // Antecedent in Sheet1
        var consequent1 = data1[j][1]; // Consequent in Sheet1
        
        if (antecedent2 === antecedent1 && consequent2 === consequent1) {
          foundInSheet1 = true;
          break;
        }
      }
      
      // If no match found, record the rule as "Not Found"
      if (!foundInSheet1) {
        differences.push(['Rule not found in Sheet1: ' + antecedent2 + ' => ' + consequent2]);
      }
    }
    
    // Output the differences to Sheet3
    if (differences.length > 0) {
      sheet3.getRange(1, 1, differences.length, 1).setValues(differences);  // Write the differences in Sheet3 starting at cell A1
    } else {
      sheet3.getRange(1, 1).setValue('All rules match between Sheet1 and Sheet2');
    }
  }
  