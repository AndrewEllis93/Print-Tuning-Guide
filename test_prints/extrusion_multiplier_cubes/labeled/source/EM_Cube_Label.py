from operator import lt
import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        design = app.activeProduct
        rootComp = design.rootComponent
        
        # Get the sketch named "ChangeText"
        sk = rootComp.sketches.itemByName('ChangeText')
        
        # Get the first sketch text.
        skText = sk.sketchTexts.item(0)

        #Prompts the user for the new Text   
        #(textBody, cancelled) = ui.inputBox('What text?', 'New text:', )
        
        # Grab the sketch and first text entity 
        sk = rootComp.sketches.itemByName('ChangeText') 
        skText = sk.sketchTexts.item(0)

        textNum = 0.500

        while textNum <= 1.500:
            # Change the text.
            textBody = "{:.3f}".format(textNum)
            #textBody = textBody.rstrip('0')
            skText.text = textBody

            # Write in the path to the folder where you want to save STL‘s
            folder = 'C:/temp/'
            
            # Construct the output filename. Name will be the same as you‘ve changed    the text into.
            filename = folder + str("EM_Cube-") + skText.text + '.stl'

            # Save the file as STL.
            exportMgr = adsk.fusion.ExportManager.cast(design.exportManager)
            stlOptions = exportMgr.createSTLExportOptions(rootComp)
            stlOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementMedium
            stlOptions.filename = filename
            exportMgr.execute(stlOptions)

            textNum = textNum + 0.005

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))