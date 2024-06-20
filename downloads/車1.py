# NX 1872
# Journal created by Admin on Thu Jun 20 17:19:09 2024 台北標準時間

#
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Assemblies
import NXOpen.Drawings
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    # ----------------------------------------------
    #   Menu: File->New...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    fileNew1 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId1, "New Dialog")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    fileNew1.TemplateFileName = "model-plain-1-mm-template.prt"
    
    fileNew1.UseBlankTemplate = False
    
    fileNew1.ApplicationName = "ModelTemplate"
    
    fileNew1.Units = NXOpen.Part.Units.Millimeters
    
    fileNew1.RelationType = ""
    
    fileNew1.UsesMasterModel = "No"
    
    fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew1.TemplatePresentationName = "Model"
    
    fileNew1.ItemType = ""
    
    fileNew1.Specialization = ""
    
    fileNew1.SetCanCreateAltrep(False)
    
    fileNew1.NewFileName = "C:\\Users\\Admin\\Desktop\\機器人組裝\model1.pr\\model1.prt"
    
    fileNew1.MasterFileName = ""
    
    fileNew1.MakeDisplayedPart = True
    
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    # User Function call - UF_PART_ask_part_name
    
    nXObject1 = fileNew1.Commit()
    
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    theSession.DeleteUndoMark(markId3, None)
    
    fileNew1.Destroy()
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    scaleAboutPoint1 = NXOpen.Point3d(16.519315060614431, 4.4248165340931598, 0.0)
    viewCenter1 = NXOpen.Point3d(-16.519315060614431, -4.4248165340931598, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(20.649143825768036, 5.531020667616418, 0.0)
    viewCenter2 = NXOpen.Point3d(-20.649143825768036, -5.531020667616481, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(25.811429782210045, 6.9137758345205613, 0.0)
    viewCenter3 = NXOpen.Point3d(-25.811429782210045, -6.9137758345205613, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(32.264287227762551, 8.6422197931507512, 0.0)
    viewCenter4 = NXOpen.Point3d(-32.264287227762551, -8.6422197931507014, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(48.252393845091376, 12.963329689726052, 0.0)
    viewCenter5 = NXOpen.Point3d(-48.252393845091376, -12.963329689726052, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(44.363394938173535, 10.370663751780842, 0.0)
    viewCenter6 = NXOpen.Point3d(-44.363394938173585, -10.370663751780842, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(38.717144673315062, 8.2965310014246736, 0.0)
    viewCenter7 = NXOpen.Point3d(-38.717144673315225, -8.2965310014246736, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(32.079919872175346, 6.6372248011397392, 0.0)
    viewCenter8 = NXOpen.Point3d(-32.079919872175473, -6.6372248011397392, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(25.958923666679809, 5.3097798409118182, 0.0)
    viewCenter9 = NXOpen.Point3d(-25.958923666679933, -5.3097798409117924, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(20.767138933343805, 4.247823872729434, 0.0)
    viewCenter10 = NXOpen.Point3d(-20.767138933343986, -4.2478238727294135, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(16.613711146675012, 3.398259098183563, 0.0)
    viewCenter11 = NXOpen.Point3d(-16.613711146675204, -3.398259098183531, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(16.991295490917697, 3.0678727969712649, 0.0)
    viewCenter12 = NXOpen.Point3d(-16.991295490917796, -3.0678727969712449, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(16.224327291674854, 3.2448654583350014, 0.0)
    viewCenter13 = NXOpen.Point3d(-16.224327291674957, -3.2448654583349761, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(15.118123158151528, 4.0560818229187827, 0.0)
    viewCenter14 = NXOpen.Point3d(-15.118123158151652, -4.0560818229187205, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(10.140204557296721, 5.0701022786484788, 0.0)
    viewCenter15 = NXOpen.Point3d(-10.14020455729688, -5.0701022786483998, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(7.4899238207304792, 6.3376278483105493, 0.0)
    viewCenter16 = NXOpen.Point3d(-7.4899238207306755, -6.3376278483104995, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(7.9220348103880625, 7.9220348103882472, 0.0)
    viewCenter17 = NXOpen.Point3d(-7.9220348103880625, -7.9220348103881237, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(69.317804590896159, 26.106705625142837, 0.0)
    viewCenter18 = NXOpen.Point3d(-69.317804590896159, -26.106705625142684, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(82.146099596354276, 32.633382031428454, 0.0)
    viewCenter19 = NXOpen.Point3d(-82.146099596354276, -32.633382031428354, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(102.68262449544285, 40.791727539285688, 0.0)
    viewCenter20 = NXOpen.Point3d(-102.68262449544285, -40.791727539285446, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(128.35328061930355, 50.98965942410711, 0.0)
    viewCenter21 = NXOpen.Point3d(-128.35328061930355, -50.989659424106812, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint21, viewCenter21)
    
    scaleAboutPoint22 = NXOpen.Point3d(160.44160077412965, 63.737074280133889, 0.0)
    viewCenter22 = NXOpen.Point3d(-160.44160077412965, -63.737074280133704, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(200.55200096766225, 79.671342850167107, 0.0)
    viewCenter23 = NXOpen.Point3d(-200.55200096766131, -79.671342850167107, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint23, viewCenter23)
    
    scaleAboutPoint24 = NXOpen.Point3d(326.24041253301186, 127.06205540759412, 0.0)
    viewCenter24 = NXOpen.Point3d(-326.24041253301129, -127.06205540759412, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint24, viewCenter24)
    
    scaleAboutPoint25 = NXOpen.Point3d(260.99233002640949, 101.64964432607529, 0.0)
    viewCenter25 = NXOpen.Point3d(-260.99233002640852, -101.64964432607529, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint25, viewCenter25)
    
    scaleAboutPoint26 = NXOpen.Point3d(208.7938640211276, 81.319715460860237, 0.0)
    viewCenter26 = NXOpen.Point3d(-208.79386402112684, -81.319715460860237, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint26, viewCenter26)
    
    scaleAboutPoint27 = NXOpen.Point3d(172.3098835711202, 66.814036486760827, 0.0)
    viewCenter27 = NXOpen.Point3d(-172.30988357111931, -66.814036486760827, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint27, viewCenter27)
    
    scaleAboutPoint28 = NXOpen.Point3d(146.28757462364501, 54.857840483866759, 0.0)
    viewCenter28 = NXOpen.Point3d(-146.28757462364405, -54.857840483866759, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint28, viewCenter28)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.PlaneReference = plane1
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    theSession.SetUndoMarkName(markId4, "Create Sketch Dialog")
    
    datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) X axis")
    direction1 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumPlane1 = workPart.Datums.FindObject("DATUM_CSYS(0) XZ plane")
    datumCsys1 = workPart.Features.FindObject("DATUM_CSYS(0)")
    point1 = datumCsys1.FindObject("POINT 1")
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane1, direction1, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, True)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.Csystem = cartesianCoordinateSystem1
    
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane2 = workPart.Planes.CreatePlane(origin2, normal2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane2.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom1 = [NXOpen.NXObject.Null] * 1 
    geom1[0] = datumPlane1
    plane2.SetGeometry(geom1)
    
    plane2.SetFlip(True)
    
    plane2.SetExpression(None)
    
    plane2.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane2.Evaluate()
    
    origin3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal3 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane3 = workPart.Planes.CreatePlane(origin3, normal3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane3.SynchronizeToPlane(plane2)
    
    plane3.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom2 = [NXOpen.NXObject.Null] * 1 
    geom2[0] = datumPlane1
    plane3.SetGeometry(geom2)
    
    plane3.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane3.Evaluate()
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.DeleteUndoMark(markId5, None)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject2 = sketchInPlaceBuilder1.Commit()
    
    sketch1 = nXObject2
    feature1 = sketch1.Feature
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId7)
    
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId6, None)
    
    theSession.SetUndoMarkName(markId4, "Create Sketch")
    
    sketchInPlaceBuilder1.Destroy()
    
    sketchAlongPathBuilder1.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression2)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression1)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane1.DestroyPlane()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression4)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression3)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane3.DestroyPlane()
    
    scaleAboutPoint29 = NXOpen.Point3d(92.273700916453024, 7.8770232489655152, 0.0)
    viewCenter29 = NXOpen.Point3d(-92.273700916452455, -7.8770232489654193, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint29, viewCenter29)
    
    scaleAboutPoint30 = NXOpen.Point3d(62.11595476327097, 3.6009249138128947, 0.0)
    viewCenter30 = NXOpen.Point3d(-62.115954763270359, -3.600924913812741, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint30, viewCenter30)
    
    scaleAboutPoint31 = NXOpen.Point3d(49.692763810616903, 2.8807399310503157, 0.0)
    viewCenter31 = NXOpen.Point3d(-49.692763810616164, -2.8807399310501927, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(39.754211048493623, 2.3045919448402525, 0.0)
    viewCenter32 = NXOpen.Point3d(-39.754211048492834, -2.3045919448402037, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(31.803368838795013, 1.8436735558722022, 0.0)
    viewCenter33 = NXOpen.Point3d(-31.80336883879415, -1.8436735558721236, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint33, viewCenter33)
    
    scaleAboutPoint34 = NXOpen.Point3d(25.442695071036109, 1.4749388446977618, 0.0)
    viewCenter34 = NXOpen.Point3d(-25.442695071035228, -1.474938844697699, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint34, viewCenter34)
    
    scaleAboutPoint35 = NXOpen.Point3d(9.7345963750053812, 2.6548899204559469, 0.0)
    viewCenter35 = NXOpen.Point3d(-9.734596375004525, -2.6548899204558714, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint35, viewCenter35)
    
    scaleAboutPoint36 = NXOpen.Point3d(11.799510757582192, 3.3186124005699336, 0.0)
    viewCenter36 = NXOpen.Point3d(-11.799510757581279, -3.3186124005698074, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint36, viewCenter36)
    
    scaleAboutPoint37 = NXOpen.Point3d(14.749388446977582, 4.1482655007123777, 0.0)
    viewCenter37 = NXOpen.Point3d(-14.749388446976717, -4.1482655007122986, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint37, viewCenter37)
    
    scaleAboutPoint38 = NXOpen.Point3d(18.436735558721928, 5.1853318758905207, 0.0)
    viewCenter38 = NXOpen.Point3d(-18.436735558721043, -5.1853318758903733, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint38, viewCenter38)
    
    scaleAboutPoint39 = NXOpen.Point3d(23.04591944840228, 6.4816648448630874, 0.0)
    viewCenter39 = NXOpen.Point3d(-23.045919448401296, -6.4816648448629648, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint39, viewCenter39)
    
    scaleAboutPoint40 = NXOpen.Point3d(28.807399310502696, 8.102081056078859, 0.0)
    viewCenter40 = NXOpen.Point3d(-28.807399310501776, -8.1020810560787062, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint40, viewCenter40)
    
    scaleAboutPoint41 = NXOpen.Point3d(77.64494345408869, 23.631069746896443, 0.0)
    viewCenter41 = NXOpen.Point3d(-77.644943454087738, -23.631069746896348, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint41, viewCenter41)
    
    scaleAboutPoint42 = NXOpen.Point3d(62.115954763271127, 18.904855797517236, 0.0)
    viewCenter42 = NXOpen.Point3d(-62.115954763270203, -18.904855797517083, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint42, viewCenter42)
    
    scaleAboutPoint43 = NXOpen.Point3d(49.692763810617024, 15.12388463801379, 0.0)
    viewCenter43 = NXOpen.Point3d(-49.692763810616043, -15.123884638013665, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint43, viewCenter43)
    
    scaleAboutPoint44 = NXOpen.Point3d(39.754211048493715, 12.099107710411031, 0.0)
    viewCenter44 = NXOpen.Point3d(-39.754211048492834, -12.099107710410934, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint44, viewCenter44)
    
    scaleAboutPoint45 = NXOpen.Point3d(16.132143613881691, 5.0701022786485161, 0.0)
    viewCenter45 = NXOpen.Point3d(-16.132143613880825, -5.0701022786483589, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint45, viewCenter45)
    
    scaleAboutPoint46 = NXOpen.Point3d(20.165179517352012, 6.3376278483106443, 0.0)
    viewCenter46 = NXOpen.Point3d(-20.165179517351127, -6.3376278483104977, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint46, viewCenter46)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Profile...
    # ----------------------------------------------
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId9, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    endPoint1 = NXOpen.Point3d(-185.0, 0.0, 4.3343848489553395e-13)
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)
    
    theSession.ActiveSketch.AddGeometry(line1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_1.Geometry = line1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys2 = workPart.Features.FindObject("SKETCH(1:1B)")
    point2 = datumCsys2.FindObject("POINT 1")
    geom2_1.Geometry = point2
    geom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_1, geom2_1)
    
    geom3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom3.Geometry = line1
    geom3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint2 = theSession.ActiveSketch.CreateHorizontalConstraint(geom3)
    
    dimObject1_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_1.Geometry = line1
    dimObject1_1.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_1.AssocValue = 0
    dimObject1_1.HelpPoint.X = 0.0
    dimObject1_1.HelpPoint.Y = 0.0
    dimObject1_1.HelpPoint.Z = 0.0
    dimObject1_1.View = NXOpen.NXObject.Null
    dimObject2_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_1.Geometry = line1
    dimObject2_1.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_1.AssocValue = 0
    dimObject2_1.HelpPoint.X = 0.0
    dimObject2_1.HelpPoint.Y = 0.0
    dimObject2_1.HelpPoint.Z = 0.0
    dimObject2_1.View = NXOpen.NXObject.Null
    dimOrigin1 = NXOpen.Point3d(-92.499999999999943, 0.0, 24.497630909718733)
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_1, dimObject2_1, dimOrigin1, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint1 = sketchDimensionalConstraint1
    dimension1 = sketchHelpedDimensionalConstraint1.AssociatedDimension
    
    expression5 = sketchHelpedDimensionalConstraint1.AssociatedExpression
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False
    
    theSession.ActiveSketch.Update()
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = True
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId10, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint2 = NXOpen.Point3d(-185.0, 0.0, 4.3343848489553395e-13)
    endPoint2 = NXOpen.Point3d(-184.99999999999994, 0.0, 60.000000000000433)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)
    
    theSession.ActiveSketch.AddGeometry(line2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_2.Geometry = line2
    geom1_2.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_2.SplineDefiningPointIndex = 0
    geom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_2.Geometry = line1
    geom2_2.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint3 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_2, geom2_2)
    
    geom4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom4.Geometry = line2
    geom4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint4 = theSession.ActiveSketch.CreateVerticalConstraint(geom4)
    
    dimObject1_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_2.Geometry = line2
    dimObject1_2.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_2.AssocValue = 0
    dimObject1_2.HelpPoint.X = 0.0
    dimObject1_2.HelpPoint.Y = 0.0
    dimObject1_2.HelpPoint.Z = 0.0
    dimObject1_2.View = NXOpen.NXObject.Null
    dimObject2_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_2.Geometry = line2
    dimObject2_2.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_2.AssocValue = 0
    dimObject2_2.HelpPoint.X = 0.0
    dimObject2_2.HelpPoint.Y = 0.0
    dimObject2_2.HelpPoint.Z = 0.0
    dimObject2_2.View = NXOpen.NXObject.Null
    dimOrigin2 = NXOpen.Point3d(-160.50236909028146, 0.0, 30.000000000000409)
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_2, dimObject2_2, dimOrigin2, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint2 = sketchDimensionalConstraint2
    dimension2 = sketchHelpedDimensionalConstraint2.AssociatedDimension
    
    expression6 = sketchHelpedDimensionalConstraint2.AssociatedExpression
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False
    
    theSession.ActiveSketch.Update()
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = True
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId11, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint3 = NXOpen.Point3d(-184.99999999999994, 0.0, 60.000000000000433)
    endPoint3 = NXOpen.Point3d(-131.20188195964062, 0.0, 71.435142994977184)
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)
    
    theSession.ActiveSketch.AddGeometry(line3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_3.Geometry = line3
    geom1_3.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_3.SplineDefiningPointIndex = 0
    geom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_3.Geometry = line2
    geom2_3.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint5 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_3, geom2_3)
    
    dimObject1_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_3.Geometry = line3
    dimObject1_3.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_3.AssocValue = 0
    dimObject1_3.HelpPoint.X = 0.0
    dimObject1_3.HelpPoint.Y = 0.0
    dimObject1_3.HelpPoint.Z = 0.0
    dimObject1_3.View = NXOpen.NXObject.Null
    dimObject2_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_3.Geometry = line3
    dimObject2_3.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_3.AssocValue = 0
    dimObject2_3.HelpPoint.X = 0.0
    dimObject2_3.HelpPoint.Y = 0.0
    dimObject2_3.HelpPoint.Z = 0.0
    dimObject2_3.View = NXOpen.NXObject.Null
    dimOrigin3 = NXOpen.Point3d(-153.00759711635129, 0.0, 41.755272599485323)
    sketchDimensionalConstraint3 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_3, dimObject2_3, dimOrigin3, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint3 = sketchDimensionalConstraint3
    dimension3 = sketchHelpedDimensionalConstraint3.AssociatedDimension
    
    expression7 = sketchHelpedDimensionalConstraint3.AssociatedExpression
    
    dimObject1_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_4.Geometry = line2
    dimObject1_4.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_4.AssocValue = 0
    dimObject1_4.HelpPoint.X = -185.0
    dimObject1_4.HelpPoint.Y = 0.0
    dimObject1_4.HelpPoint.Z = 4.3343848489553395e-13
    dimObject1_4.View = NXOpen.NXObject.Null
    dimObject2_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_4.Geometry = line3
    dimObject2_4.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_4.AssocValue = 0
    dimObject2_4.HelpPoint.X = -131.20188195964062
    dimObject2_4.HelpPoint.Y = 0.0
    dimObject2_4.HelpPoint.Z = 71.435142994977184
    dimObject2_4.View = NXOpen.NXObject.Null
    dimOrigin4 = NXOpen.Point3d(-165.96176507324876, 0.0, 44.583141336101775)
    sketchDimensionalConstraint4 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.AngularDim, dimObject1_4, dimObject2_4, dimOrigin4, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension4 = sketchDimensionalConstraint4.AssociatedDimension
    
    expression8 = sketchDimensionalConstraint4.AssociatedExpression
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False
    
    theSession.ActiveSketch.Update()
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = True
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId12, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(-112.49895684332581, -0.0, -16.555201642561173)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 89.956101279119778, ( 31.166878311919241 * math.pi/180.0 ), ( 101.99999999999962 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_4.Geometry = arc1
    geom1_4.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_4.SplineDefiningPointIndex = 0
    geom2_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_4.Geometry = line3
    geom2_4.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint6 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_4, geom2_4)
    
    geom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_5.Geometry = arc1
    geom1_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom1_5.SplineDefiningPointIndex = 0
    geom1Help1 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom1Help1.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom1Help1.Point.X = -131.20188195964062
    geom1Help1.Point.Y = 0.0
    geom1Help1.Point.Z = 71.435142994977184
    geom1Help1.Parameter = 0.0
    geom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_5.Geometry = line2
    geom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_5.SplineDefiningPointIndex = 0
    geom2Help1 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    geom2Help1.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    geom2Help1.Point.X = -131.20188195964062
    geom2Help1.Point.Y = 0.0
    geom2Help1.Point.Z = 71.435142994977184
    geom2Help1.Parameter = 0.0
    sketchTangentConstraint1 = theSession.ActiveSketch.CreateTangentConstraint(geom1_5, geom1Help1, geom2_5, geom2Help1)
    
    geom1_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_6.Geometry = arc1
    geom1_6.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_6.SplineDefiningPointIndex = 0
    geom2_6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_6.Geometry = line3
    geom2_6.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_6.SplineDefiningPointIndex = 0
    try:
        # Constraint already exists.
        sketchGeometricConstraint7 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_6, geom2_6)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(910023)
        
    dimObject1_5 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_5.Geometry = arc1
    dimObject1_5.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_5.AssocValue = 0
    dimObject1_5.HelpPoint.X = 0.0
    dimObject1_5.HelpPoint.Y = 0.0
    dimObject1_5.HelpPoint.Z = 0.0
    dimObject1_5.View = NXOpen.NXObject.Null
    dimOrigin5 = NXOpen.Point3d(-104.88736730440887, 0.0, 28.519961038382171)
    sketchDimensionalConstraint5 = theSession.ActiveSketch.CreateRadialDimension(dimObject1_5, dimOrigin5, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension5 = sketchDimensionalConstraint5.AssociatedDimension
    
    expression9 = sketchDimensionalConstraint5.AssociatedExpression
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False
    
    theSession.ActiveSketch.Update()
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = True
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    scaleAboutPoint47 = NXOpen.Point3d(-57.614798621004276, 28.087214327739897, 0.0)
    viewCenter47 = NXOpen.Point3d(57.614798621005136, -28.087214327739652, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint47, viewCenter47)
    
    scaleAboutPoint48 = NXOpen.Point3d(-46.091838896803274, 22.469771462191918, 0.0)
    viewCenter48 = NXOpen.Point3d(46.091838896804163, -22.469771462191723, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint48, viewCenter48)
    
    scaleAboutPoint49 = NXOpen.Point3d(-36.873471117442584, 17.975817169753576, 0.0)
    viewCenter49 = NXOpen.Point3d(36.873471117443444, -17.975817169753338, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint49, viewCenter49)
    
    scaleAboutPoint50 = NXOpen.Point3d(-34.661062850396007, 11.062041335232989, 0.0)
    viewCenter50 = NXOpen.Point3d(34.661062850396789, -11.062041335232768, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint50, viewCenter50)
    
    theSession.SetUndoMarkVisibility(markId13, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint4 = NXOpen.Point3d(-18.071739095729356, 0.0, 35.621051782465173)
    endPoint4 = NXOpen.Point3d(0.0, 0.0, 30.000000000000217)
    line4 = workPart.Curves.CreateLine(startPoint4, endPoint4)
    
    theSession.ActiveSketch.AddGeometry(line4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_7.Geometry = line4
    geom1_7.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_7.SplineDefiningPointIndex = 0
    geom2_7 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_7.Geometry = arc1
    geom2_7.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_7.SplineDefiningPointIndex = 0
    sketchGeometricConstraint8 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_7, geom2_7)
    
    dimObject1_6 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_6.Geometry = line4
    dimObject1_6.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_6.AssocValue = 0
    dimObject1_6.HelpPoint.X = 0.0
    dimObject1_6.HelpPoint.Y = 0.0
    dimObject1_6.HelpPoint.Z = 0.0
    dimObject1_6.View = NXOpen.NXObject.Null
    dimObject2_5 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_5.Geometry = line4
    dimObject2_5.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_5.AssocValue = 0
    dimObject2_5.HelpPoint.X = 0.0
    dimObject2_5.HelpPoint.Y = 0.0
    dimObject2_5.HelpPoint.Z = 0.0
    dimObject2_5.View = NXOpen.NXObject.Null
    dimOrigin6 = NXOpen.Point3d(-12.016091051757776, 0.0, 23.229083209304513)
    sketchDimensionalConstraint6 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_6, dimObject2_5, dimOrigin6, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint4 = sketchDimensionalConstraint6
    dimension6 = sketchHelpedDimensionalConstraint4.AssociatedDimension
    
    expression10 = sketchHelpedDimensionalConstraint4.AssociatedExpression
    
    dimObject1_7 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_7.Geometry = line3
    dimObject1_7.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_7.AssocValue = 0
    dimObject1_7.HelpPoint.X = -184.99999999999994
    dimObject1_7.HelpPoint.Y = 0.0
    dimObject1_7.HelpPoint.Z = 60.000000000000433
    dimObject1_7.View = NXOpen.NXObject.Null
    dimObject2_6 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_6.Geometry = line4
    dimObject2_6.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_6.AssocValue = 0
    dimObject2_6.HelpPoint.X = 0.0
    dimObject2_6.HelpPoint.Y = 0.0
    dimObject2_6.HelpPoint.Z = 30.000000000000217
    dimObject2_6.View = NXOpen.NXObject.Null
    dimOrigin7 = NXOpen.Point3d(-138.37188136448052, 0.0, -58.443921217699284)
    sketchDimensionalConstraint7 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.AngularDim, dimObject1_7, dimObject2_6, dimOrigin7, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension7 = sketchDimensionalConstraint7.AssociatedDimension
    
    expression11 = sketchDimensionalConstraint7.AssociatedExpression
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False
    
    theSession.ActiveSketch.Update()
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = True
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId14, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint5 = NXOpen.Point3d(0.0, 0.0, 30.000000000000217)
    endPoint5 = NXOpen.Point3d(-5.8801615778171037e-14, 0.0, 0.0)
    line5 = workPart.Curves.CreateLine(startPoint5, endPoint5)
    
    theSession.ActiveSketch.AddGeometry(line5, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_8.Geometry = line5
    geom1_8.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_8.SplineDefiningPointIndex = 0
    geom2_8 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_8.Geometry = line4
    geom2_8.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_8.SplineDefiningPointIndex = 0
    sketchGeometricConstraint9 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_8, geom2_8)
    
    geom5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom5.Geometry = line5
    geom5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint10 = theSession.ActiveSketch.CreateVerticalConstraint(geom5)
    
    geom1_9 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_9.Geometry = line5
    geom1_9.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_9.SplineDefiningPointIndex = 0
    geom2_9 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_9.Geometry = point2
    geom2_9.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_9.SplineDefiningPointIndex = 0
    sketchGeometricConstraint11 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_9, geom2_9)
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = False
    
    theSession.ActiveSketch.Update()
    
    theSession.ActiveSketch.Preferences.ContinuousAutoDimensioningSetting = True
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.ActiveSketch.Update()
    
    scaleAboutPoint51 = NXOpen.Point3d(-22.419070439404965, 16.519315060614588, 0.0)
    viewCenter51 = NXOpen.Point3d(22.419070439405722, -16.51931506061436, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint51, viewCenter51)
    
    scaleAboutPoint52 = NXOpen.Point3d(-28.023838049256334, 20.649143825768171, 0.0)
    viewCenter52 = NXOpen.Point3d(28.023838049256991, -20.64914382576795, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint52, viewCenter52)
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.DeleteUndoMark(markId16, "Curve")
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete1 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects1 = [NXOpen.TaggedObject.Null] * 1 
    objects1[0] = line3
    nErrs2 = theSession.UpdateManager.AddObjectsToDeleteList(objects1)
    
    notifyOnDelete2 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs3 = theSession.UpdateManager.DoUpdate(id1)
    
    theSession.DeleteUndoMark(markId17, None)
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId20, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    perpendicularDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 2 1")
    theSession.UpdateManager.LogForUpdate(perpendicularDimension1)
    
    radiusDimension1 = dimension5
    theSession.UpdateManager.LogForUpdate(radiusDimension1)
    
    center2 = NXOpen.Point3d(-97.37154774941628, 0.0, -1.6654872272293915)
    arc1.SetParameters(87.628452250583734, center2, ( 25.182772933766586 * math.pi/180.0 ), ( 131.43560743660717 * math.pi/180.0 ))
    
    helpPoint1_1 = NXOpen.Point3d(-185.0, 0.0, -1.665487227229308)
    helpPoint2_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchTangentConstraint1.SetHelpPoints(True, False, helpPoint1_1, helpPoint2_1)
    
    sketchHelpedDimensionalConstraint5 = theSession.ActiveSketch.FindObject("ENTITY 243 1 1")
    sketchHelpedDimensionalConstraint5.Refresh()
    
    nErrs4 = theSession.UpdateManager.DoUpdate(markId20)
    
    geoms1 = [NXOpen.SmartObject.Null] * 1 
    geoms1[0] = arc1
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms1)
    
    geoms2 = [NXOpen.SmartObject.Null] * 1 
    geoms2[0] = arc1
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms2)
    
    geoms3 = [NXOpen.SmartObject.Null] * 1 
    geoms3[0] = arc1
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms3)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Line...
    # ----------------------------------------------
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId22, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint6 = NXOpen.Point3d(-184.99999999999994, 0.0, 60.000000000000433)
    endPoint6 = NXOpen.Point3d(-155.36212146194768, 0.0, 60.000000000000433)
    line6 = workPart.Curves.CreateLine(startPoint6, endPoint6)
    
    theSession.ActiveSketch.AddGeometry(line6, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_10 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_10.Geometry = line6
    geom1_10.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_10.SplineDefiningPointIndex = 0
    geom2_10 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_10.Geometry = line2
    geom2_10.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_10.SplineDefiningPointIndex = 0
    sketchGeometricConstraint12 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_10, geom2_10)
    
    geom6 = NXOpen.Sketch.ConstraintGeometry()
    
    geom6.Geometry = line6
    geom6.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom6.SplineDefiningPointIndex = 0
    sketchGeometricConstraint13 = theSession.ActiveSketch.CreateHorizontalConstraint(geom6)
    
    dimObject1_8 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_8.Geometry = line6
    dimObject1_8.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_8.AssocValue = 0
    dimObject1_8.HelpPoint.X = 0.0
    dimObject1_8.HelpPoint.Y = 0.0
    dimObject1_8.HelpPoint.Z = 0.0
    dimObject1_8.View = NXOpen.NXObject.Null
    dimObject2_7 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_7.Geometry = line6
    dimObject2_7.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_7.AssocValue = 0
    dimObject2_7.HelpPoint.X = 0.0
    dimObject2_7.HelpPoint.Y = 0.0
    dimObject2_7.HelpPoint.Z = 0.0
    dimObject2_7.View = NXOpen.NXObject.Null
    dimOrigin8 = NXOpen.Point3d(-170.1810607309738, 0.0, 44.321516217780584)
    sketchDimensionalConstraint8 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_8, dimObject2_7, dimOrigin8, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint6 = sketchDimensionalConstraint8
    dimension8 = sketchHelpedDimensionalConstraint6.AssociatedDimension
    
    expression12 = sketchHelpedDimensionalConstraint6.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   Dialog Begin Line
    # ----------------------------------------------
    scaleAboutPoint53 = NXOpen.Point3d(-197.27307047831965, 44.248165340931699, 0.0)
    viewCenter53 = NXOpen.Point3d(197.27307047832031, -44.248165340931457, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint53, viewCenter53)
    
    scaleAboutPoint54 = NXOpen.Point3d(-156.71225224913232, 35.398532272745385, 0.0)
    viewCenter54 = NXOpen.Point3d(156.712252249133, -35.398532272745129, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint54, viewCenter54)
    
    scaleAboutPoint55 = NXOpen.Point3d(-125.36980179930582, 28.318825818196313, 0.0)
    viewCenter55 = NXOpen.Point3d(125.36980179930647, -28.318825818196089, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint55, viewCenter55)
    
    scaleAboutPoint56 = NXOpen.Point3d(-100.29584143944459, 22.89105086970871, 0.0)
    viewCenter56 = NXOpen.Point3d(100.29584143944527, -22.891050869708511, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint56, viewCenter56)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    geom1_11 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_11.Geometry = arc1
    geom1_11.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_11.SplineDefiningPointIndex = 0
    geom2_11 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_11.Geometry = line6
    geom2_11.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_11.SplineDefiningPointIndex = 0
    sketchGeometricConstraint14 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_11, geom2_11)
    
    theSession.SetUndoMarkVisibility(markId24, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    theSession.UpdateManager.LogForUpdate(perpendicularDimension1)
    
    theSession.UpdateManager.LogForUpdate(radiusDimension1)
    
    center3 = NXOpen.Point3d(-96.303296107577381, 0.0, -6.175225191472002)
    arc1.SetParameters(88.696703892422619, center3, ( 28.113969824160097 * math.pi/180.0 ), ( 131.74767644359758 * math.pi/180.0 ))
    
    helpPoint1_2 = NXOpen.Point3d(-185.0, 0.0, -6.1752251914719185)
    helpPoint2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchTangentConstraint1.SetHelpPoints(True, False, helpPoint1_2, helpPoint2_2)
    
    sketchHelpedDimensionalConstraint5.Refresh()
    
    nErrs5 = theSession.UpdateManager.DoUpdate(markId24)
    
    geoms4 = [NXOpen.SmartObject.Null] * 1 
    geoms4[0] = arc1
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms4)
    
    geoms5 = [NXOpen.SmartObject.Null] * 1 
    geoms5[0] = arc1
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms5)
    
    geoms6 = [NXOpen.SmartObject.Null] * 1 
    geoms6[0] = arc1
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms6)
    
    scaleAboutPoint57 = NXOpen.Point3d(-26.808488441225418, 13.215452048491668, 0.0)
    viewCenter57 = NXOpen.Point3d(26.808488441226093, -13.215452048491475, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint57, viewCenter57)
    
    scaleAboutPoint58 = NXOpen.Point3d(-21.446790752980256, 10.57236163879336, 0.0)
    viewCenter58 = NXOpen.Point3d(21.446790752980938, -10.572361638793154, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint58, viewCenter58)
    
    scaleAboutPoint59 = NXOpen.Point3d(-17.157432602384141, 8.4578893110347089, 0.0)
    viewCenter59 = NXOpen.Point3d(17.157432602384812, -8.4578893110345028, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint59, viewCenter59)
    
    scaleAboutPoint60 = NXOpen.Point3d(-8.8928664756017639, 6.4763266724494457, 0.0)
    viewCenter60 = NXOpen.Point3d(8.8928664756024389, -6.4763266724492556, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint60, viewCenter60)
    
    scaleAboutPoint61 = NXOpen.Point3d(-9.4245052322953491, 7.7329273700888752, 0.0)
    viewCenter61 = NXOpen.Point3d(9.424505232296049, -7.7329273700886789, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint61, viewCenter61)
    
    scaleAboutPoint62 = NXOpen.Point3d(-11.327530327278145, 9.5151254749140008, 0.0)
    viewCenter62 = NXOpen.Point3d(11.327530327278842, -9.5151254749138197, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint62, viewCenter62)
    
    scaleAboutPoint63 = NXOpen.Point3d(-13.970620736976466, 11.893906843642485, 0.0)
    viewCenter63 = NXOpen.Point3d(13.970620736977143, -11.893906843642309, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint63, viewCenter63)
    
    scaleAboutPoint64 = NXOpen.Point3d(-15.811344415159212, 14.867383554553086, 0.0)
    viewCenter64 = NXOpen.Point3d(15.811344415159875, -14.867383554552926, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint64, viewCenter64)
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId26, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    radiusDimension2 = theSession.ActiveSketch.FindObject("ENTITY 26 6 1")
    theSession.UpdateManager.LogForUpdate(radiusDimension2)
    
    parallelDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 2 1")
    theSession.UpdateManager.LogForUpdate(parallelDimension1)
    
    parallelDimension2 = theSession.ActiveSketch.FindObject("ENTITY 26 3 1")
    theSession.UpdateManager.LogForUpdate(parallelDimension2)
    
    minorAngularDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    theSession.UpdateManager.LogForUpdate(minorAngularDimension1)
    
    parallelDimension3 = theSession.ActiveSketch.FindObject("ENTITY 26 4 1")
    theSession.UpdateManager.LogForUpdate(parallelDimension3)
    
    startPoint7 = NXOpen.Point3d(-184.87025491893752, 0.0, -1.0669228671605788e-14)
    endPoint7 = NXOpen.Point3d(-184.87025491893752, 0.0, 60.421834436324779)
    line2.SetEndpoints(startPoint7, endPoint7)
    
    startPoint8 = NXOpen.Point3d(-184.87025491893752, 0.0, 60.421834436324779)
    endPoint8 = NXOpen.Point3d(-155.23237638088523, 0.0, 60.421834436324779)
    line6.SetEndpoints(startPoint8, endPoint8)
    
    center4 = NXOpen.Point3d(-112.34262489650833, 0.0, 1.934858670101697)
    arc1.SetParameters(72.527630022429207, center4, ( 38.774430577685813 * math.pi/180.0 ), ( 126.25339345305171 * math.pi/180.0 ))
    
    startPoint9 = NXOpen.Point3d(-55.798813688827622, 0.0, 47.355718754214337)
    endPoint9 = NXOpen.Point3d(0.0, 0.0, 30.000000000000217)
    line4.SetEndpoints(startPoint9, endPoint9)
    
    startPoint10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    endPoint10 = NXOpen.Point3d(-184.87025491893752, 0.0, -1.0669228671605788e-14)
    line1.SetEndpoints(startPoint10, endPoint10)
    
    helpPoint1_3 = NXOpen.Point3d(-184.87025491893752, 0.0, 1.934858670101697)
    helpPoint2_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchTangentConstraint1.SetHelpPoints(True, False, helpPoint1_3, helpPoint2_3)
    
    nErrs6 = theSession.UpdateManager.DoUpdate(markId26)
    
    geoms7 = [NXOpen.SmartObject.Null] * 5 
    geoms7[0] = line2
    geoms7[1] = line6
    geoms7[2] = arc1
    geoms7[3] = line4
    geoms7[4] = line1
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms7)
    
    geoms8 = [NXOpen.SmartObject.Null] * 5 
    geoms8[0] = line2
    geoms8[1] = line6
    geoms8[2] = arc1
    geoms8[3] = line4
    geoms8[4] = line1
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms8)
    
    geoms9 = [NXOpen.SmartObject.Null] * 5 
    geoms9[0] = line2
    geoms9[1] = line6
    geoms9[2] = arc1
    geoms9[3] = line4
    geoms9[4] = line1
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms9)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Constraint->Dimension->Rapid...
    # ----------------------------------------------
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder1 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    sketchRapidDimensionBuilder1.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.ModelView
    
    lines1 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBefore(lines1)
    
    lines2 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAfter(lines2)
    
    lines3 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAbove(lines3)
    
    lines4 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBelow(lines4)
    
    theSession.SetUndoMarkName(markId27, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder1.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.ModelView
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits1 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits2 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits3 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits4 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits5 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits6 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits7 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits8 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits9 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits10 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder1.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits11 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits12 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits13 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits14 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits15 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits16 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits17 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits18 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits19 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits20 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    point3 = NXOpen.Point3d(-77.167678133537166, -0.0, -7.1054273576010019e-15)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(line1, workPart.ModelingViews.WorkView, point3)
    
    point1_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line1, workPart.ModelingViews.WorkView, point1_1, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_1)
    
    point1_2 = NXOpen.Point3d(-184.87025491893752, 0.0, -1.0669228671605788e-14)
    point2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line1, workPart.ModelingViews.WorkView, point1_2, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_2)
    
    dimensionlinearunits21 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits22 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits23 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits24 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits25 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits26 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin1 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin1.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin1.View = NXOpen.View.Null
    assocOrigin1.ViewOfGeometry = workPart.ModelingViews.WorkView
    point4 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin1.PointOnGeometry = point4
    assocOrigin1.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.DimensionLine = 0
    assocOrigin1.AssociatedView = NXOpen.View.Null
    assocOrigin1.AssociatedPoint = NXOpen.Point.Null
    assocOrigin1.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.XOffsetFactor = 0.0
    assocOrigin1.YOffsetFactor = 0.0
    assocOrigin1.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder1.Origin.SetAssociativeOrigin(assocOrigin1)
    
    point5 = NXOpen.Point3d(-72.447873830504449, -0.0, -23.863180227600544)
    sketchRapidDimensionBuilder1.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point5)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.TextCentered = False
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject3 = sketchRapidDimensionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId28, None)
    
    theSession.SetUndoMarkName(markId27, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId27, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder1.Destroy()
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder2 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines5 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBefore(lines5)
    
    lines6 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAfter(lines6)
    
    lines7 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAbove(lines7)
    
    lines8 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBelow(lines8)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder2.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId29, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder2.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits27 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits28 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits29 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits30 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits31 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits32 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits33 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits34 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits35 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits36 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder2.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits37 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits38 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits39 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits40 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits41 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits42 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits43 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits44 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits45 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits46 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    expression13 = workPart.Expressions.FindObject("p0")
    expression13.SetFormula("15")
    
    theSession.SetUndoMarkVisibility(markId29, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.081137985159251524)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId30, None)
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId29, "Edit Driving Value")
    
    scaleAboutPoint65 = NXOpen.Point3d(65.192296935639462, -43.65818980305238, 0.0)
    viewCenter65 = NXOpen.Point3d(-65.192296935638808, 43.658189803052529, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint65, viewCenter65)
    
    scaleAboutPoint66 = NXOpen.Point3d(52.153837548511653, -34.926551842441889, 0.0)
    viewCenter66 = NXOpen.Point3d(-52.153837548510992, 34.926551842442052, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint66, viewCenter66)
    
    scaleAboutPoint67 = NXOpen.Point3d(41.723070038809389, -27.941241473953497, 0.0)
    viewCenter67 = NXOpen.Point3d(-41.723070038808714, 27.941241473953639, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint67, viewCenter67)
    
    scaleAboutPoint68 = NXOpen.Point3d(33.37845603104757, -22.352993179162794, 0.0)
    viewCenter68 = NXOpen.Point3d(-33.378456031046902, 22.352993179162937, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint68, viewCenter68)
    
    scaleAboutPoint69 = NXOpen.Point3d(26.70276482483813, -17.882394543330218, 0.0)
    viewCenter69 = NXOpen.Point3d(-26.702764824837452, 17.88239454333036, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint69, viewCenter69)
    
    scaleAboutPoint70 = NXOpen.Point3d(20.878903899240033, -8.2162353307192451, 0.0)
    viewCenter70 = NXOpen.Point3d(-20.878903899239358, 8.2162353307194014, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint70, viewCenter70)
    
    scaleAboutPoint71 = NXOpen.Point3d(16.780452393092972, -6.3410004434727121, 0.0)
    viewCenter71 = NXOpen.Point3d(-16.7804523930923, 6.3410004434728702, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint71, viewCenter71)
    
    scaleAboutPoint72 = NXOpen.Point3d(13.548088752395877, -4.8253466789353165, 0.0)
    viewCenter72 = NXOpen.Point3d(-13.548088752395197, 4.8253466789354746, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint72, viewCenter72)
    
    scaleAboutPoint73 = NXOpen.Point3d(10.83847100191676, -3.7612958728110972, 0.0)
    viewCenter73 = NXOpen.Point3d(-10.838471001916098, 3.7612958728112531, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint73, viewCenter73)
    
    scaleAboutPoint74 = NXOpen.Point3d(8.6707768015334743, -1.8212590542032281, 0.0)
    viewCenter74 = NXOpen.Point3d(-8.6707768015328046, 1.8212590542033866, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint74, viewCenter74)
    
    scaleAboutPoint75 = NXOpen.Point3d(4.4026958005961561, 3.3257774033278555, 0.0)
    viewCenter75 = NXOpen.Point3d(-4.402695800595481, -3.3257774033277041, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint75, viewCenter75)
    
    scaleAboutPoint76 = NXOpen.Point3d(3.4968173840706887, 2.6606219226623016, 0.0)
    viewCenter76 = NXOpen.Point3d(-3.4968173840700145, -2.6606219226621461, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint76, viewCenter76)
    
    point6 = NXOpen.Point3d(-14.999999999999799, 0.0, 3.3515144431509625)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(line2, workPart.ModelingViews.WorkView, point6)
    
    point1_3 = NXOpen.Point3d(-14.999999999999799, 0.0, 4.9025059057892726)
    point2_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line2, workPart.ModelingViews.WorkView, point1_3, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_3)
    
    point1_4 = NXOpen.Point3d(-14.999999999999799, 0.0, -8.6567971761741134e-16)
    point2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line2, workPart.ModelingViews.WorkView, point1_4, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_4)
    
    dimensionlinearunits47 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits48 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits49 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits50 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits51 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits52 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin2 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin2.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin2.View = NXOpen.View.Null
    assocOrigin2.ViewOfGeometry = workPart.ModelingViews.WorkView
    point7 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin2.PointOnGeometry = point7
    assocOrigin2.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.DimensionLine = 0
    assocOrigin2.AssociatedView = NXOpen.View.Null
    assocOrigin2.AssociatedPoint = NXOpen.Point.Null
    assocOrigin2.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.XOffsetFactor = 0.0
    assocOrigin2.YOffsetFactor = 0.0
    assocOrigin2.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder2.Origin.SetAssociativeOrigin(assocOrigin2)
    
    point8 = NXOpen.Point3d(-16.612521506583704, 0.0, 2.0946873253981408)
    sketchRapidDimensionBuilder2.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point8)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.TextCentered = True
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject4 = sketchRapidDimensionBuilder2.Commit()
    
    theSession.DeleteUndoMark(markId32, None)
    
    theSession.SetUndoMarkName(markId31, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId31, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder2.Destroy()
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder3 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines9 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBefore(lines9)
    
    lines10 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAfter(lines10)
    
    lines11 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAbove(lines11)
    
    lines12 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBelow(lines12)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder3.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId33, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder3.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits53 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits54 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits55 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits56 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits57 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits58 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits59 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits60 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits61 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits62 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder3.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits63 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits64 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits65 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits66 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits67 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits68 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits69 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits70 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits71 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits72 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    expression14 = workPart.Expressions.FindObject("p1")
    expression14.SetFormula("3.5")
    
    theSession.SetUndoMarkVisibility(markId33, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId34, None)
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId33, "Edit Driving Value")
    
    verticalDimension1 = nXObject4
    point9 = NXOpen.Point3d(-16.497126645599874, 0.0, 1.6689878177721851)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(verticalDimension1, workPart.ModelingViews.WorkView, point9)
    
    point1_5 = NXOpen.Point3d(-14.999999999999799, 0.0, -8.6567971761741134e-16)
    point2_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line2, NXOpen.View.Null, point1_5, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_5)
    
    point1_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_6, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_6)
    
    sketchRapidDimensionBuilder3.FirstAssociativity.Value = NXOpen.TaggedObject.Null
    
    expression14.SetFormula("4")
    
    theSession.SetUndoMarkVisibility(markId35, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId36, None)
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId35, "Edit Driving Value")
    
    point10 = NXOpen.Point3d(-1.7763568394002505e-15, 0.0, 1.6689878177721851)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(line5, workPart.ModelingViews.WorkView, point10)
    
    point1_7 = NXOpen.Point3d(0.0, 0.0, 2.4341395547775635)
    point2_7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line5, workPart.ModelingViews.WorkView, point1_7, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_7)
    
    point1_8 = NXOpen.Point3d(-4.771044628349252e-15, 0.0, 0.0)
    point2_8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line5, workPart.ModelingViews.WorkView, point1_8, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_8)
    
    dimensionlinearunits73 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits74 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits75 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits76 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits77 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits78 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin3 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin3.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin3.View = NXOpen.View.Null
    assocOrigin3.ViewOfGeometry = workPart.ModelingViews.WorkView
    point11 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin3.PointOnGeometry = point11
    assocOrigin3.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.DimensionLine = 0
    assocOrigin3.AssociatedView = NXOpen.View.Null
    assocOrigin3.AssociatedPoint = NXOpen.Point.Null
    assocOrigin3.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.XOffsetFactor = 0.0
    assocOrigin3.YOffsetFactor = 0.0
    assocOrigin3.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder3.Origin.SetAssociativeOrigin(assocOrigin3)
    
    point12 = NXOpen.Point3d(2.8682988185850355, 0.0, 1.3446453357714563)
    sketchRapidDimensionBuilder3.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point12)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.TextCentered = True
    
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject5 = sketchRapidDimensionBuilder3.Commit()
    
    theSession.DeleteUndoMark(markId38, None)
    
    theSession.SetUndoMarkName(markId37, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId37, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder3.Destroy()
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder4 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines13 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBefore(lines13)
    
    lines14 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAfter(lines14)
    
    lines15 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAbove(lines15)
    
    lines16 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBelow(lines16)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder4.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId39, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder4.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits79 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits80 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits81 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits82 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits83 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits84 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits85 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits86 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits87 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits88 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder4.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits89 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits90 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits91 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits92 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits93 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits94 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits95 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits96 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits97 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits98 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    expression15 = workPart.Expressions.FindObject("p2")
    expression15.SetFormula("2")
    
    theSession.SetUndoMarkVisibility(markId39, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId40, None)
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId39, "Edit Driving Value")
    
    point13 = NXOpen.Point3d(-3.2879430145112218, 0.0, 3.0226850799726872)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(line4, workPart.ModelingViews.WorkView, point13)
    
    point1_9 = NXOpen.Point3d(-4.527403316987936, 0.0, 3.4082080507075694)
    point2_9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line4, workPart.ModelingViews.WorkView, point1_9, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_9)
    
    point1_10 = NXOpen.Point3d(0.0, 0.0, 2.0)
    point2_10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line4, workPart.ModelingViews.WorkView, point1_10, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_10)
    
    dimensionlinearunits99 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits100 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits101 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits102 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits103 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits104 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin4 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin4.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin4.View = NXOpen.View.Null
    assocOrigin4.ViewOfGeometry = workPart.ModelingViews.WorkView
    point14 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin4.PointOnGeometry = point14
    assocOrigin4.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin4.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin4.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.DimensionLine = 0
    assocOrigin4.AssociatedView = NXOpen.View.Null
    assocOrigin4.AssociatedPoint = NXOpen.Point.Null
    assocOrigin4.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin4.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin4.XOffsetFactor = 0.0
    assocOrigin4.YOffsetFactor = 0.0
    assocOrigin4.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder4.Origin.SetAssociativeOrigin(assocOrigin4)
    
    point15 = NXOpen.Point3d(-1.9765670063008445, 0.0, 4.2231848635279192)
    sketchRapidDimensionBuilder4.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point15)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.TextCentered = True
    
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject6 = sketchRapidDimensionBuilder4.Commit()
    
    theSession.DeleteUndoMark(markId42, None)
    
    theSession.SetUndoMarkName(markId41, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId41, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder4.Destroy()
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder5 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines17 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBefore(lines17)
    
    lines18 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAfter(lines18)
    
    lines19 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAbove(lines19)
    
    lines20 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBelow(lines20)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder5.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId43, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder5.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits105 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits106 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits107 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits108 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits109 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits110 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits111 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits112 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits113 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits114 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder5.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits115 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits116 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits117 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits118 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits119 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits120 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits121 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits122 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits123 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits124 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    expression16 = workPart.Expressions.FindObject("p3")
    expression16.SetFormula("4")
    
    theSession.SetUndoMarkVisibility(markId43, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId44, None)
    
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId43, "Edit Driving Value")
    
    scaleAboutPoint77 = NXOpen.Point3d(1.1960129023780219, 2.7366396918812224, 0.0)
    viewCenter77 = NXOpen.Point3d(-1.1960129023773443, -2.7366396918810652, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint77, viewCenter77)
    
    scaleAboutPoint78 = NXOpen.Point3d(0.95681032190248816, 2.2055288776050315, 0.0)
    viewCenter78 = NXOpen.Point3d(-0.95681032190180637, -2.2055288776048751, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint78, viewCenter78)
    
    scaleAboutPoint79 = NXOpen.Point3d(0.76544825752206036, 1.7644231020840413, 0.0)
    viewCenter79 = NXOpen.Point3d(-0.7654482575213768, -1.764423102083883, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint79, viewCenter79)
    
    scaleAboutPoint80 = NXOpen.Point3d(0.61235860601771741, 1.4115384816672498, 0.0)
    viewCenter80 = NXOpen.Point3d(-0.6123586060170324, -1.4115384816670924, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint80, viewCenter80)
    
    scaleAboutPoint81 = NXOpen.Point3d(0.76544825752205925, 1.7644231020840413, 0.0)
    viewCenter81 = NXOpen.Point3d(-0.7654482575213768, -1.764423102083883, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint81, viewCenter81)
    
    scaleAboutPoint82 = NXOpen.Point3d(0.95681032190248816, 2.2055288776050315, 0.0)
    viewCenter82 = NXOpen.Point3d(-0.95681032190180504, -2.2055288776048738, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint82, viewCenter82)
    
    scaleAboutPoint83 = NXOpen.Point3d(1.196012902378025, 2.7569110970062694, 0.0)
    viewCenter83 = NXOpen.Point3d(-1.1960129023773372, -2.7569110970061086, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint83, viewCenter83)
    
    scaleAboutPoint84 = NXOpen.Point3d(1.4950161279724494, 3.44613887125782, 0.0)
    viewCenter84 = NXOpen.Point3d(-1.495016127971758, -3.4461388712576557, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint84, viewCenter84)
    
    scaleAboutPoint85 = NXOpen.Point3d(1.8687701599654749, 4.3076735890722526, 0.0)
    viewCenter85 = NXOpen.Point3d(-1.8687701599647837, -4.307673589072091, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint85, viewCenter85)
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = 0.91275089512988516
    rotMatrix1.Xy = 0.40819659584968659
    rotMatrix1.Xz = -0.01616609341556011
    rotMatrix1.Yx = -0.10172140845180329
    rotMatrix1.Yy = 0.26542493614973378
    rotMatrix1.Yz = 0.95875041503641156
    rotMatrix1.Zx = 0.395649539999953
    rotMatrix1.Zy = -0.8734558617392395
    rotMatrix1.Zz = 0.28378918071552389
    translation1 = NXOpen.Point3d(4.7637145454537322, -2.0856690677694472, 14.228407635556502)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 6.6826480863576805)
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder5.Destroy()
    
    theSession.UndoToMark(markId45, None)
    
    theSession.DeleteUndoMark(markId45, None)
    
    sketchRapidDimensionBuilder5.Destroy()
    
    sketch2 = theSession.ActiveSketch
    
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    scaleAboutPoint86 = NXOpen.Point3d(-13.503468426797683, -3.3758671066994927, 0.0)
    viewCenter86 = NXOpen.Point3d(13.503468426798259, 3.3758671066995887, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint86, viewCenter86)
    
    scaleAboutPoint87 = NXOpen.Point3d(-10.802774741438146, -2.7006936853595174, 0.0)
    viewCenter87 = NXOpen.Point3d(10.80277474143853, 2.700693685359671, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint87, viewCenter87)
    
    scaleAboutPoint88 = NXOpen.Point3d(-8.6422197931504563, -2.1605549482876141, 0.0)
    viewCenter88 = NXOpen.Point3d(8.6422197931509466, 2.1605549482877366, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint88, viewCenter88)
    
    scaleAboutPoint89 = NXOpen.Point3d(-6.913775834520365, -1.7284439586300913, 0.0)
    viewCenter89 = NXOpen.Point3d(6.9137758345207576, 1.7284439586301403, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint89, viewCenter89)
    
    scaleAboutPoint90 = NXOpen.Point3d(-5.5310206676162919, -1.382755166904073, 0.0)
    viewCenter90 = NXOpen.Point3d(5.5310206676166063, 1.3827551669041516, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint90, viewCenter90)
    
    scaleAboutPoint91 = NXOpen.Point3d(-30.973715738651961, -2.949877689395398, 0.0)
    viewCenter91 = NXOpen.Point3d(30.973715738652274, 2.949877689395461, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint91, viewCenter91)
    
    scaleAboutPoint92 = NXOpen.Point3d(-22.714058208344706, -1.4749388446976865, 0.0)
    viewCenter92 = NXOpen.Point3d(22.714058208345108, 1.474938844697737, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint92, viewCenter92)
    
    scaleAboutPoint93 = NXOpen.Point3d(-11.327530327278291, -0.70797064545488564, 0.0)
    viewCenter93 = NXOpen.Point3d(11.327530327278692, 0.70797064545494592, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint93, viewCenter93)
    
    scaleAboutPoint94 = NXOpen.Point3d(-5.8525573357603653, -0.5663765163638923, 0.0)
    viewCenter94 = NXOpen.Point3d(5.8525573357607517, 0.56637651636395669, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint94, viewCenter94)
    
    scaleAboutPoint95 = NXOpen.Point3d(-4.3799783932141656, -0.4531012130911139, 0.0)
    viewCenter95 = NXOpen.Point3d(4.3799783932145386, 0.45310121309116541, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint95, viewCenter95)
    
    scaleAboutPoint96 = NXOpen.Point3d(-11.720218045290631, 2.5373667933104027, 0.0)
    viewCenter96 = NXOpen.Point3d(11.720218045291002, -2.5373667933103614, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint96, viewCenter96)
    
    scaleAboutPoint97 = NXOpen.Point3d(-8.9895280677280471, 1.5465854740177845, 0.0)
    viewCenter97 = NXOpen.Point3d(8.9895280677283935, -1.5465854740177349, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint97, viewCenter97)
    
    scaleAboutPoint98 = NXOpen.Point3d(-7.191622454182399, 1.2372683792142343, 0.0)
    viewCenter98 = NXOpen.Point3d(7.1916224541827551, -1.2372683792141947, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint98, viewCenter98)
    
    scaleAboutPoint99 = NXOpen.Point3d(-5.7532979633458767, 0.98981470337138744, 0.0)
    viewCenter99 = NXOpen.Point3d(5.7532979633462356, -0.98981470337134514, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint99, viewCenter99)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit2 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression17 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("25")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId47, "Extrude Dialog")
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("25")
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features1 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature1 = feature1
    features1[0] = sketchFeature1
    curveFeatureRule1 = workPart.ScRuleFactory.CreateRuleCurveFeature(features1)
    
    section1.AllowSelfIntersection(True)
    
    rules1 = [None] * 1 
    rules1[0] = curveFeatureRule1
    helpPoint1 = NXOpen.Point3d(-6.5818178033780939, 0.0, 5.6436080641891921)
    section1.AddToSection(rules1, arc1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId49, None)
    
    direction2 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    expression18 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId48, None)
    
    extrudeBuilder1.Limits.SymmetricOption = True
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("25")
    
    extrudeBuilder1.Limits.StartExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.Symmetric
    
    extrudeBuilder1.Limits.EndExtend.TrimType = NXOpen.GeometricUtilities.Extend.ExtendType.Symmetric
    
    extrudeBuilder1.Limits.StartExtend.Target = NXOpen.DisplayableObject.Null
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("5")
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("5")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("4")
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("4")
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = 0.36191080625221017
    rotMatrix2.Xy = 0.92852730429093455
    rotMatrix2.Xz = -0.082810708873232927
    rotMatrix2.Yx = -0.33647689730130342
    rotMatrix2.Yy = 0.21295720885330988
    rotMatrix2.Yz = 0.91729631242030862
    rotMatrix2.Zx = 0.86936980963245225
    rotMatrix2.Zy = -0.30411555761522646
    rotMatrix2.Zz = 0.38949950156067803
    translation2 = NXOpen.Point3d(-11.656987248464223, -7.1937760953500565, 5.5164659698193113)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 5.3461184690861359)
    
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    feature2 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId50, None)
    
    theSession.SetUndoMarkName(markId47, "Extrude")
    
    expression19 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression17)
    
    workPart.Expressions.Delete(expression18)
    
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder2.Section = section2
    
    extrudeBuilder2.AllowSelfIntersectingSection(True)
    
    expression20 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder2.DistanceTolerance = 0.01
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies2)
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("4")
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("4")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies3 = [NXOpen.Body.Null] * 1 
    targetBodies3[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies3)
    
    extrudeBuilder2.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder2.Offset.EndOffset.SetFormula("5")
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("4")
    
    smartVolumeProfileBuilder2 = extrudeBuilder2.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId51, "Extrude Dialog")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   Dialog Begin Extrude
    # ----------------------------------------------
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = 0.62022956825370357
    rotMatrix3.Xy = 0.78393498521846539
    rotMatrix3.Xz = 0.027590244912860371
    rotMatrix3.Yx = -0.24294300652414449
    rotMatrix3.Yy = 0.15852921503997261
    rotMatrix3.Yz = 0.9569990509712224
    rotMatrix3.Zx = 0.74585117700841463
    rotMatrix3.Zy = -0.60026196525295317
    rotMatrix3.Zz = 0.28877602882827519
    translation3 = NXOpen.Point3d(-10.065028687033983, -6.6164973130380904, 4.9052286301582875)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 5.3461184690861359)
    
    extrudeBuilder2.Destroy()
    
    section2.Destroy()
    
    workPart.Expressions.Delete(expression20)
    
    theSession.UndoToMark(markId51, None)
    
    theSession.DeleteUndoMark(markId51, None)
    
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects2 = [NXOpen.DisplayableObject.Null] * 7 
    objects2[0] = line6
    objects2[1] = line2
    objects2[2] = line5
    objects2[3] = line4
    objects2[4] = line1
    objects2[5] = sketch2
    objects2[6] = arc1
    theSession.DisplayManager.BlankObjects(objects2)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = 0.84951580141998795
    rotMatrix4.Xy = 0.50688035912767748
    rotMatrix4.Xz = 0.14627099735885998
    rotMatrix4.Yx = -0.42689501041425071
    rotMatrix4.Yy = 0.49755908752437189
    rotMatrix4.Yz = 0.75511297466361571
    rotMatrix4.Zx = 0.30997347180230844
    rotMatrix4.Zy = -0.70392276277480548
    rotMatrix4.Zz = 0.63906900318065241
    translation4 = NXOpen.Point3d(-8.7144520420969105, -7.3683176359430105, 0.5468144900411287)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 5.346118469086135)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder1 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData1 = edgeBlendBuilder1.LimitsListData
    
    origin4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal4 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane4 = workPart.Planes.CreatePlane(origin4, normal4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder1 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression23 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression24 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId53, "Edge Blend Dialog")
    
    scCollector1 = workPart.ScCollectors.CreateCollector()
    
    seedEdges1 = [NXOpen.Edge.Null] * 1 
    extrude1 = feature2
    edge1 = extrude1.FindObject("EDGE * 150 * 160 {(-15,-4,4)(-15,0,4)(-15,4,4) EXTRUDE(2)}")
    seedEdges1[0] = edge1
    edgeMultipleSeedTangentRule1 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges1, 0.5, True)
    
    rules2 = [None] * 1 
    rules2[0] = edgeMultipleSeedTangentRule1
    scCollector1.ReplaceRules(rules2, False)
    
    scCollector1.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    seedEdges2 = [NXOpen.Edge.Null] * 2 
    seedEdges2[0] = edge1
    edge2 = extrude1.FindObject("EDGE * 140 * 190 {(-4,-4,3.2441639961022)(-4,0,3.2441639961022)(-4,4,3.2441639961022) EXTRUDE(2)}")
    seedEdges2[1] = edge2
    edgeMultipleSeedTangentRule2 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges2, 0.5, True)
    
    rules3 = [None] * 1 
    rules3[0] = edgeMultipleSeedTangentRule2
    scCollector1.ReplaceRules(rules3, False)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = 0.99133600696283664
    rotMatrix5.Xy = 0.040475423388539607
    rotMatrix5.Xz = 0.1249586387590024
    rotMatrix5.Yx = -0.12918126747283795
    rotMatrix5.Yy = 0.12825730889908638
    rotMatrix5.Yz = 0.98329154519302087
    rotMatrix5.Zx = 0.023772282875136698
    rotMatrix5.Zy = -0.99091462942853392
    rotMatrix5.Zz = 0.13237475496265086
    translation5 = NXOpen.Point3d(-7.584523920382817, -5.8450479375708868, -0.023990743412110854)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 5.346118469086135)
    
    scCollector1.Destroy()
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder1)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression24)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression23)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression21)
    
    workPart.Expressions.Delete(expression22)
    
    theSession.UndoToMark(markId53, None)
    
    theSession.DeleteUndoMark(markId53, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder2 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression25 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression26 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData2 = edgeBlendBuilder2.LimitsListData
    
    origin5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane5 = workPart.Planes.CreatePlane(origin5, normal5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder2 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression28 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId54, "Edge Blend Dialog")
    
    scCollector2 = workPart.ScCollectors.CreateCollector()
    
    seedEdges3 = [NXOpen.Edge.Null] * 1 
    seedEdges3[0] = edge1
    edgeMultipleSeedTangentRule3 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges3, 0.5, True)
    
    rules4 = [None] * 1 
    rules4[0] = edgeMultipleSeedTangentRule3
    scCollector2.ReplaceRules(rules4, False)
    
    scCollector2.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    scCollector2.Destroy()
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder2)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression28)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression27)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression25)
    
    workPart.Expressions.Delete(expression26)
    
    theSession.UndoToMark(markId54, None)
    
    theSession.DeleteUndoMark(markId54, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder3 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData3 = edgeBlendBuilder3.LimitsListData
    
    origin6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal6 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane6 = workPart.Planes.CreatePlane(origin6, normal6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder3 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression31 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression32 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId55, "Edge Blend Dialog")
    
    scCollector3 = workPart.ScCollectors.CreateCollector()
    
    seedEdges4 = [NXOpen.Edge.Null] * 1 
    seedEdges4[0] = edge1
    edgeMultipleSeedTangentRule4 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges4, 0.5, True)
    
    rules5 = [None] * 1 
    rules5[0] = edgeMultipleSeedTangentRule4
    scCollector3.ReplaceRules(rules5, False)
    
    scCollector3.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    scCollector3.Destroy()
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder3)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression32)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression31)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression29)
    
    workPart.Expressions.Delete(expression30)
    
    theSession.UndoToMark(markId55, None)
    
    theSession.DeleteUndoMark(markId55, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder4 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression33 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression34 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData4 = edgeBlendBuilder4.LimitsListData
    
    origin7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal7 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane7 = workPart.Planes.CreatePlane(origin7, normal7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder4 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression35 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression36 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId56, "Edge Blend Dialog")
    
    scCollector4 = workPart.ScCollectors.CreateCollector()
    
    seedEdges5 = [NXOpen.Edge.Null] * 1 
    seedEdges5[0] = edge1
    edgeMultipleSeedTangentRule5 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges5, 0.5, True)
    
    rules6 = [None] * 1 
    rules6[0] = edgeMultipleSeedTangentRule5
    scCollector4.ReplaceRules(rules6, False)
    
    scCollector4.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    scaleAboutPoint100 = NXOpen.Point3d(-18.954951569561452, -2.3755552880912538, 0.0)
    viewCenter100 = NXOpen.Point3d(18.954951569561821, 2.3755552880912965, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint100, viewCenter100)
    
    scaleAboutPoint101 = NXOpen.Point3d(-23.136918691305468, -2.7838538532319421, 0.0)
    viewCenter101 = NXOpen.Point3d(23.136918691305834, 2.7838538532319843, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint101, viewCenter101)
    
    scaleAboutPoint102 = NXOpen.Point3d(-28.225184900823891, -3.3251587691381475, 0.0)
    viewCenter102 = NXOpen.Point3d(28.225184900824257, 3.3251587691381932, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint102, viewCenter102)
    
    scaleAboutPoint103 = NXOpen.Point3d(-34.508188389021015, -3.673140500792154, 0.0)
    viewCenter103 = NXOpen.Point3d(34.508188389021392, 3.6731405007921953, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint103, viewCenter103)
    
    scaleAboutPoint104 = NXOpen.Point3d(-42.651927525645782, -4.2289446555172807, 0.0)
    viewCenter104 = NXOpen.Point3d(42.651927525646151, 4.2289446555173216, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint104, viewCenter104)
    
    scaleAboutPoint105 = NXOpen.Point3d(-34.121542020516586, -3.3831557244138248, 0.0)
    viewCenter105 = NXOpen.Point3d(34.121542020516955, 3.3831557244138657, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint105, viewCenter105)
    
    scaleAboutPoint106 = NXOpen.Point3d(-27.297233616413234, -2.7065245795310466, 0.0)
    viewCenter106 = NXOpen.Point3d(27.297233616413603, 2.7065245795310928, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint106, viewCenter106)
    
    scaleAboutPoint107 = NXOpen.Point3d(-21.837786893130549, -2.1652196636248426, 0.0)
    viewCenter107 = NXOpen.Point3d(21.837786893130925, 2.1652196636248795, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint107, viewCenter107)
    
    scaleAboutPoint108 = NXOpen.Point3d(-17.4702295145044, -1.7321757308998698, 0.0)
    viewCenter108 = NXOpen.Point3d(17.47022951450478, 1.7321757308999035, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint108, viewCenter108)
    
    scaleAboutPoint109 = NXOpen.Point3d(-13.976183611603481, -1.3857405847198927, 0.0)
    viewCenter109 = NXOpen.Point3d(13.976183611603863, 1.3857405847199231, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint109, viewCenter109)
    
    scaleAboutPoint110 = NXOpen.Point3d(-11.180946889282746, -1.108592467775914, 0.0)
    viewCenter110 = NXOpen.Point3d(11.180946889283126, 1.1085924677759411, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint110, viewCenter110)
    
    rotMatrix6 = NXOpen.Matrix3x3()
    
    rotMatrix6.Xx = 0.99434203516211506
    rotMatrix6.Xy = 0.017335623658245179
    rotMatrix6.Xz = 0.10480168539698734
    rotMatrix6.Yx = -0.10563975310465436
    rotMatrix6.Yy = 0.057887351710017368
    rotMatrix6.Yz = 0.99271813576462509
    rotMatrix6.Zx = 0.011142695977952767
    rotMatrix6.Zy = -0.99817259562882599
    rotMatrix6.Zz = 0.059391158112656522
    translation6 = NXOpen.Point3d(-0.0085145259653858218, -5.3904442552756429, 0.071757916468888863)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation6, 10.441637634933858)
    
    rotMatrix7 = NXOpen.Matrix3x3()
    
    rotMatrix7.Xx = 0.98937473848117063
    rotMatrix7.Xy = -0.085286063537372878
    rotMatrix7.Xz = 0.11774512398236016
    rotMatrix7.Yx = -0.092995956773895883
    rotMatrix7.Yy = 0.25129233980155025
    rotMatrix7.Yz = 0.9634333977918631
    rotMatrix7.Zx = -0.11175588968385394
    rotMatrix7.Zy = -0.96414648644454914
    rotMatrix7.Zz = 0.24069103389534249
    translation7 = NXOpen.Point3d(-0.079548677175378835, -5.2191892879520854, -1.3231328504206836)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix7, translation7, 10.441637634933858)
    
    seedEdges6 = [NXOpen.Edge.Null] * 2 
    seedEdges6[0] = edge1
    edge3 = extrude1.FindObject("EDGE * 140 * 150 {(-13.7192233438236,-4,4)(-13.7192233438236,0,4)(-13.7192233438236,4,4) EXTRUDE(2)}")
    seedEdges6[1] = edge3
    edgeMultipleSeedTangentRule6 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges6, 0.5, True)
    
    rules7 = [None] * 1 
    rules7[0] = edgeMultipleSeedTangentRule6
    scCollector4.ReplaceRules(rules7, False)
    
    seedEdges7 = [NXOpen.Edge.Null] * 3 
    seedEdges7[0] = edge1
    seedEdges7[1] = edge3
    seedEdges7[2] = edge2
    edgeMultipleSeedTangentRule7 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges7, 0.5, True)
    
    rules8 = [None] * 1 
    rules8[0] = edgeMultipleSeedTangentRule7
    scCollector4.ReplaceRules(rules8, False)
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    theSession.DeleteUndoMark(markId57, None)
    
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder4.Tolerance = 0.01
    
    edgeBlendBuilder4.AllInstancesOption = False
    
    edgeBlendBuilder4.RemoveSelfIntersection = True
    
    edgeBlendBuilder4.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder4.LimitFailingAreas = True
    
    edgeBlendBuilder4.ConvexConcaveY = False
    
    edgeBlendBuilder4.RollOverSmoothEdge = True
    
    edgeBlendBuilder4.RollOntoEdge = True
    
    edgeBlendBuilder4.MoveSharpEdge = True
    
    edgeBlendBuilder4.TrimmingOption = False
    
    edgeBlendBuilder4.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder4.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder4.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder4.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex1 = edgeBlendBuilder4.AddChainset(scCollector4, "0.01")
    
    feature3 = edgeBlendBuilder4.CommitFeature()
    
    theSession.DeleteUndoMark(markId58, None)
    
    theSession.SetUndoMarkName(markId56, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder4)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression36)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression35)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder4.Destroy()
    
    workPart.Expressions.Delete(expression33)
    
    workPart.Expressions.Delete(expression34)
    
    rotMatrix8 = NXOpen.Matrix3x3()
    
    rotMatrix8.Xx = 0.99417569216579493
    rotMatrix8.Xy = -0.029495500859320581
    rotMatrix8.Xz = 0.10365668591908231
    rotMatrix8.Yx = -0.092995956773895883
    rotMatrix8.Yy = 0.25129233980155025
    rotMatrix8.Yz = 0.9634333977918631
    rotMatrix8.Zx = -0.054465081753147959
    rotMatrix8.Zy = -0.96746171778842383
    rotMatrix8.Zz = 0.24708577353523009
    translation8 = NXOpen.Point3d(0.00027030839237696114, -5.2191892879520854, -0.91333797445448051)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix8, translation8, 10.441637634933858)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete3 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId60 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects3 = [NXOpen.TaggedObject.Null] * 1 
    edgeBlend1 = feature3
    objects3[0] = edgeBlend1
    nErrs7 = theSession.UpdateManager.AddObjectsToDeleteList(objects3)
    
    notifyOnDelete4 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id2 = theSession.NewestVisibleUndoMark
    
    nErrs8 = theSession.UpdateManager.DoUpdate(id2)
    
    theSession.DeleteUndoMark(markId59, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId61 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder5 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression37 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression38 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData5 = edgeBlendBuilder5.LimitsListData
    
    origin8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal8 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane8 = workPart.Planes.CreatePlane(origin8, normal8, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder5 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression39 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression40 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId61, "Edge Blend Dialog")
    
    scCollector5 = workPart.ScCollectors.CreateCollector()
    
    seedEdges8 = [NXOpen.Edge.Null] * 1 
    seedEdges8[0] = edge1
    edgeMultipleSeedTangentRule8 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges8, 0.5, True)
    
    rules9 = [None] * 1 
    rules9[0] = edgeMultipleSeedTangentRule8
    scCollector5.ReplaceRules(rules9, False)
    
    scCollector5.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    markId62 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    theSession.DeleteUndoMark(markId62, None)
    
    markId63 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder5.Tolerance = 0.01
    
    edgeBlendBuilder5.AllInstancesOption = False
    
    edgeBlendBuilder5.RemoveSelfIntersection = True
    
    edgeBlendBuilder5.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder5.LimitFailingAreas = True
    
    edgeBlendBuilder5.ConvexConcaveY = False
    
    edgeBlendBuilder5.RollOverSmoothEdge = True
    
    edgeBlendBuilder5.RollOntoEdge = True
    
    edgeBlendBuilder5.MoveSharpEdge = True
    
    edgeBlendBuilder5.TrimmingOption = False
    
    edgeBlendBuilder5.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder5.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder5.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder5.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex2 = edgeBlendBuilder5.AddChainset(scCollector5, "0.2")
    
    feature4 = edgeBlendBuilder5.CommitFeature()
    
    theSession.DeleteUndoMark(markId63, None)
    
    theSession.SetUndoMarkName(markId61, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder5)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression40)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression39)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder5.Destroy()
    
    workPart.Expressions.Delete(expression37)
    
    workPart.Expressions.Delete(expression38)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId64 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete5 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId65 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects4 = [NXOpen.TaggedObject.Null] * 1 
    edgeBlend2 = feature4
    objects4[0] = edgeBlend2
    nErrs9 = theSession.UpdateManager.AddObjectsToDeleteList(objects4)
    
    notifyOnDelete6 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id3 = theSession.NewestVisibleUndoMark
    
    nErrs10 = theSession.UpdateManager.DoUpdate(id3)
    
    theSession.DeleteUndoMark(markId64, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId66 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder6 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression41 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression42 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData6 = edgeBlendBuilder6.LimitsListData
    
    origin9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal9 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane9 = workPart.Planes.CreatePlane(origin9, normal9, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder6 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression43 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression44 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId66, "Edge Blend Dialog")
    
    scCollector6 = workPart.ScCollectors.CreateCollector()
    
    seedEdges9 = [NXOpen.Edge.Null] * 1 
    seedEdges9[0] = edge1
    edgeMultipleSeedTangentRule9 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges9, 0.5, True)
    
    rules10 = [None] * 1 
    rules10[0] = edgeMultipleSeedTangentRule9
    scCollector6.ReplaceRules(rules10, False)
    
    scCollector6.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    seedEdges10 = [NXOpen.Edge.Null] * 2 
    seedEdges10[0] = edge1
    seedEdges10[1] = edge3
    edgeMultipleSeedTangentRule10 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges10, 0.5, True)
    
    rules11 = [None] * 1 
    rules11[0] = edgeMultipleSeedTangentRule10
    scCollector6.ReplaceRules(rules11, False)
    
    seedEdges11 = [NXOpen.Edge.Null] * 3 
    seedEdges11[0] = edge1
    seedEdges11[1] = edge3
    seedEdges11[2] = edge2
    edgeMultipleSeedTangentRule11 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges11, 0.5, True)
    
    rules12 = [None] * 1 
    rules12[0] = edgeMultipleSeedTangentRule11
    scCollector6.ReplaceRules(rules12, False)
    
    seedEdges12 = [NXOpen.Edge.Null] * 4 
    seedEdges12[0] = edge1
    seedEdges12[1] = edge3
    seedEdges12[2] = edge2
    edge4 = extrude1.FindObject("EDGE * 180 * 190 {(-0,-4,2)(-0,0,2)(-0,4,2) EXTRUDE(2)}")
    seedEdges12[3] = edge4
    edgeMultipleSeedTangentRule12 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges12, 0.5, True)
    
    rules13 = [None] * 1 
    rules13[0] = edgeMultipleSeedTangentRule12
    scCollector6.ReplaceRules(rules13, False)
    
    seedEdges13 = [NXOpen.Edge.Null] * 5 
    seedEdges13[0] = edge1
    seedEdges13[1] = edge3
    seedEdges13[2] = edge2
    seedEdges13[3] = edge4
    edge5 = extrude1.FindObject("EDGE * 130 * 140 {(-4,-4,3.2441639961022)(-8.6589920980417,-4,6.2018300327189)(-13.7192233438236,-4,4) EXTRUDE(2)}")
    seedEdges13[4] = edge5
    edgeMultipleSeedTangentRule13 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges13, 0.5, True)
    
    rules14 = [None] * 1 
    rules14[0] = edgeMultipleSeedTangentRule13
    scCollector6.ReplaceRules(rules14, False)
    
    seedEdges14 = [NXOpen.Edge.Null] * 6 
    seedEdges14[0] = edge1
    seedEdges14[1] = edge3
    seedEdges14[2] = edge2
    seedEdges14[3] = edge4
    seedEdges14[4] = edge5
    edge6 = extrude1.FindObject("EDGE * 130 * 150 {(-13.7192233438236,-4,4)(-14.3596116719118,-4,4)(-15,-4,4) EXTRUDE(2)}")
    seedEdges14[5] = edge6
    edgeMultipleSeedTangentRule14 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges14, 0.5, True)
    
    rules15 = [None] * 1 
    rules15[0] = edgeMultipleSeedTangentRule14
    scCollector6.ReplaceRules(rules15, False)
    
    rotMatrix9 = NXOpen.Matrix3x3()
    
    rotMatrix9.Xx = 0.98413718373557857
    rotMatrix9.Xy = 0.17314631583586104
    rotMatrix9.Xz = 0.038656912725653622
    rotMatrix9.Yx = -0.10323645093151804
    rotMatrix9.Yy = 0.38171527720790105
    rotMatrix9.Yz = 0.91849642478627191
    rotMatrix9.Zx = 0.14427833790307862
    rotMatrix9.Zy = -0.90791728723412413
    rotMatrix9.Zz = 0.39353520903899047
    translation9 = NXOpen.Point3d(0.12684834010878543, -5.1587769514898358, 0.24743062682545225)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix9, translation9, 10.441637634933858)
    
    seedEdges15 = [NXOpen.Edge.Null] * 7 
    seedEdges15[0] = edge1
    seedEdges15[1] = edge3
    seedEdges15[2] = edge2
    seedEdges15[3] = edge4
    seedEdges15[4] = edge5
    seedEdges15[5] = edge6
    edge7 = extrude1.FindObject("EDGE * 130 * 190 {(-0,-4,2)(-2,-4,2.6220819980511)(-4,-4,3.2441639961022) EXTRUDE(2)}")
    seedEdges15[6] = edge7
    edgeMultipleSeedTangentRule15 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges15, 0.5, True)
    
    rules16 = [None] * 1 
    rules16[0] = edgeMultipleSeedTangentRule15
    scCollector6.ReplaceRules(rules16, False)
    
    rotMatrix10 = NXOpen.Matrix3x3()
    
    rotMatrix10.Xx = 0.98764005357067908
    rotMatrix10.Xy = -0.063788835752569051
    rotMatrix10.Xz = 0.14317160687875471
    rotMatrix10.Yx = -0.04827808829261155
    rotMatrix10.Yy = 0.74522385699613358
    rotMatrix10.Yz = 0.66506437970667398
    rotMatrix10.Zx = -0.14911857957251215
    rotMatrix10.Zy = -0.66375627107933666
    rotMatrix10.Zz = 0.7329333270012609
    translation10 = NXOpen.Point3d(-0.17671584387948869, -3.9134807595085981, -3.1841278696395561)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix10, translation10, 10.441637634933858)
    
    seedEdges16 = [NXOpen.Edge.Null] * 8 
    seedEdges16[0] = edge1
    seedEdges16[1] = edge3
    seedEdges16[2] = edge2
    seedEdges16[3] = edge4
    seedEdges16[4] = edge5
    seedEdges16[5] = edge6
    seedEdges16[6] = edge7
    edge8 = extrude1.FindObject("EDGE * 120 * 150 {(-13.7192233438236,4,4)(-14.3596116719118,4,4)(-15,4,4) EXTRUDE(2)}")
    seedEdges16[7] = edge8
    edgeMultipleSeedTangentRule16 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges16, 0.5, True)
    
    rules17 = [None] * 1 
    rules17[0] = edgeMultipleSeedTangentRule16
    scCollector6.ReplaceRules(rules17, False)
    
    seedEdges17 = [NXOpen.Edge.Null] * 9 
    seedEdges17[0] = edge1
    seedEdges17[1] = edge3
    seedEdges17[2] = edge2
    seedEdges17[3] = edge4
    seedEdges17[4] = edge5
    seedEdges17[5] = edge6
    seedEdges17[6] = edge7
    seedEdges17[7] = edge8
    edge9 = extrude1.FindObject("EDGE * 120 * 140 {(-4,4,3.2441639961022)(-8.6589920980417,4,6.2018300327189)(-13.7192233438236,4,4) EXTRUDE(2)}")
    seedEdges17[8] = edge9
    edgeMultipleSeedTangentRule17 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges17, 0.5, True)
    
    rules18 = [None] * 1 
    rules18[0] = edgeMultipleSeedTangentRule17
    scCollector6.ReplaceRules(rules18, False)
    
    seedEdges18 = [NXOpen.Edge.Null] * 10 
    seedEdges18[0] = edge1
    seedEdges18[1] = edge3
    seedEdges18[2] = edge2
    seedEdges18[3] = edge4
    seedEdges18[4] = edge5
    seedEdges18[5] = edge6
    seedEdges18[6] = edge7
    seedEdges18[7] = edge8
    seedEdges18[8] = edge9
    edge10 = extrude1.FindObject("EDGE * 120 * 190 {(-0,4,2)(-2,4,2.6220819980511)(-4,4,3.2441639961022) EXTRUDE(2)}")
    seedEdges18[9] = edge10
    edgeMultipleSeedTangentRule18 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges18, 0.5, True)
    
    rules19 = [None] * 1 
    rules19[0] = edgeMultipleSeedTangentRule18
    scCollector6.ReplaceRules(rules19, False)
    
    rotMatrix11 = NXOpen.Matrix3x3()
    
    rotMatrix11.Xx = 0.8275896221246255
    rotMatrix11.Xy = 0.49511332545230147
    rotMatrix11.Xz = -0.26449614800822668
    rotMatrix11.Yx = 0.12415120492964395
    rotMatrix11.Yy = 0.29807682887695364
    rotMatrix11.Yz = 0.94643366508233528
    rotMatrix11.Zx = 0.54743209228738499
    rotMatrix11.Zy = -0.8160961947259836
    rotMatrix11.Zz = 0.18521637424275839
    translation11 = NXOpen.Point3d(-0.1925678343911077, -3.401010733849275, 4.1728684138460661)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix11, translation11, 10.441637634933858)
    
    seedEdges19 = [NXOpen.Edge.Null] * 11 
    seedEdges19[0] = edge1
    seedEdges19[1] = edge3
    seedEdges19[2] = edge2
    seedEdges19[3] = edge4
    seedEdges19[4] = edge5
    seedEdges19[5] = edge6
    seedEdges19[6] = edge7
    seedEdges19[7] = edge8
    seedEdges19[8] = edge9
    seedEdges19[9] = edge10
    edge11 = extrude1.FindObject("EDGE * 130 * 180 {(-0,-4,0)(-0,-4,1)(-0,-4,2) EXTRUDE(2)}")
    seedEdges19[10] = edge11
    edgeMultipleSeedTangentRule19 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges19, 0.5, True)
    
    rules20 = [None] * 1 
    rules20[0] = edgeMultipleSeedTangentRule19
    scCollector6.ReplaceRules(rules20, False)
    
    seedEdges20 = [NXOpen.Edge.Null] * 12 
    seedEdges20[0] = edge1
    seedEdges20[1] = edge3
    seedEdges20[2] = edge2
    seedEdges20[3] = edge4
    seedEdges20[4] = edge5
    seedEdges20[5] = edge6
    seedEdges20[6] = edge7
    seedEdges20[7] = edge8
    seedEdges20[8] = edge9
    seedEdges20[9] = edge10
    seedEdges20[10] = edge11
    edge12 = extrude1.FindObject("EDGE * 120 * 180 {(-0,4,0)(-0,4,1)(-0,4,2) EXTRUDE(2)}")
    seedEdges20[11] = edge12
    edgeMultipleSeedTangentRule20 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges20, 0.5, True)
    
    rules21 = [None] * 1 
    rules21[0] = edgeMultipleSeedTangentRule20
    scCollector6.ReplaceRules(rules21, False)
    
    rotMatrix12 = NXOpen.Matrix3x3()
    
    rotMatrix12.Xx = 0.98288700678668206
    rotMatrix12.Xy = -0.16403792371689307
    rotMatrix12.Xz = -0.083813432530682005
    rotMatrix12.Yx = 0.12896466336527038
    rotMatrix12.Yy = 0.28788192286853376
    rotMatrix12.Yz = 0.94894262950328201
    rotMatrix12.Zx = -0.13153420655102144
    rotMatrix12.Zy = -0.94351235183656945
    rotMatrix12.Zz = 0.30411049708753385
    translation12 = NXOpen.Point3d(0.48758342682247147, -3.3700136127802058, -1.7160123566656442)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix12, translation12, 10.441637634933858)
    
    seedEdges21 = [NXOpen.Edge.Null] * 13 
    seedEdges21[0] = edge1
    seedEdges21[1] = edge3
    seedEdges21[2] = edge2
    seedEdges21[3] = edge4
    seedEdges21[4] = edge5
    seedEdges21[5] = edge6
    seedEdges21[6] = edge7
    seedEdges21[7] = edge8
    seedEdges21[8] = edge9
    seedEdges21[9] = edge10
    seedEdges21[10] = edge11
    seedEdges21[11] = edge12
    edge13 = extrude1.FindObject("EDGE * 130 * 160 {(-15,-4,4)(-14.9999999999999,-4,2)(-14.9999999999998,-4,-0) EXTRUDE(2)}")
    seedEdges21[12] = edge13
    edgeMultipleSeedTangentRule21 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges21, 0.5, True)
    
    rules22 = [None] * 1 
    rules22[0] = edgeMultipleSeedTangentRule21
    scCollector6.ReplaceRules(rules22, False)
    
    seedEdges22 = [NXOpen.Edge.Null] * 14 
    seedEdges22[0] = edge1
    seedEdges22[1] = edge3
    seedEdges22[2] = edge2
    seedEdges22[3] = edge4
    seedEdges22[4] = edge5
    seedEdges22[5] = edge6
    seedEdges22[6] = edge7
    seedEdges22[7] = edge8
    seedEdges22[8] = edge9
    seedEdges22[9] = edge10
    seedEdges22[10] = edge11
    seedEdges22[11] = edge12
    seedEdges22[12] = edge13
    edge14 = extrude1.FindObject("EDGE * 120 * 160 {(-15,4,4)(-14.9999999999999,4,2)(-14.9999999999998,4,-0) EXTRUDE(2)}")
    seedEdges22[13] = edge14
    edgeMultipleSeedTangentRule22 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges22, 0.5, True)
    
    rules23 = [None] * 1 
    rules23[0] = edgeMultipleSeedTangentRule22
    scCollector6.ReplaceRules(rules23, False)
    
    markId67 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder6.Tolerance = 0.01
    
    edgeBlendBuilder6.AllInstancesOption = False
    
    edgeBlendBuilder6.RemoveSelfIntersection = True
    
    edgeBlendBuilder6.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder6.LimitFailingAreas = True
    
    edgeBlendBuilder6.ConvexConcaveY = False
    
    edgeBlendBuilder6.RollOverSmoothEdge = True
    
    edgeBlendBuilder6.RollOntoEdge = True
    
    edgeBlendBuilder6.MoveSharpEdge = True
    
    edgeBlendBuilder6.TrimmingOption = False
    
    edgeBlendBuilder6.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder6.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder6.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder6.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex3 = edgeBlendBuilder6.AddChainset(scCollector6, "0.5")
    
    feature5 = edgeBlendBuilder6.CommitFeature()
    
    theSession.DeleteUndoMark(markId67, None)
    
    theSession.SetUndoMarkName(markId66, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder6)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression44)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression43)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder6.Destroy()
    
    workPart.Expressions.Delete(expression41)
    
    workPart.Expressions.Delete(expression42)
    
    markId68 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder7 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression45 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression46 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData7 = edgeBlendBuilder7.LimitsListData
    
    origin10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal10 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane10 = workPart.Planes.CreatePlane(origin10, normal10, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder7 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression47 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression48 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId68, "Edge Blend Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Edge Blend
    # ----------------------------------------------
    scaleAboutPoint111 = NXOpen.Point3d(-12.821663741591122, -1.5963731535973216, 0.0)
    viewCenter111 = NXOpen.Point3d(12.821663741591497, 1.5963731535973498, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint111, viewCenter111)
    
    scaleAboutPoint112 = NXOpen.Point3d(-10.520859259898453, -0.9527560408771264, 0.0)
    viewCenter112 = NXOpen.Point3d(10.520859259898828, 0.95275604087715404, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint112, viewCenter112)
    
    scaleAboutPoint113 = NXOpen.Point3d(-8.4329045320187603, -0.64868496400144271, 0.0)
    viewCenter113 = NXOpen.Point3d(8.4329045320191351, 0.64868496400147035, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint113, viewCenter113)
    
    scaleAboutPoint114 = NXOpen.Point3d(-6.7463236256149699, -0.51894797120115188, 0.0)
    viewCenter114 = NXOpen.Point3d(6.7463236256153456, 0.51894797120117853, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint114, viewCenter114)
    
    scaleAboutPoint115 = NXOpen.Point3d(-8.5139901525189394, -0.63246783990140698, 0.0)
    viewCenter115 = NXOpen.Point3d(8.5139901525193178, 0.63246783990143329, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint115, viewCenter115)
    
    scaleAboutPoint116 = NXOpen.Point3d(-10.703301906023857, -0.79058479987676233, 0.0)
    viewCenter116 = NXOpen.Point3d(10.703301906024233, 0.79058479987678998, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint116, viewCenter116)
    
    scaleAboutPoint117 = NXOpen.Point3d(-13.379127382529871, -0.93755248703334193, 0.0)
    viewCenter117 = NXOpen.Point3d(13.379127382530244, 0.93755248703337002, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint117, viewCenter117)
    
    scaleAboutPoint118 = NXOpen.Point3d(-16.75558329867027, -1.1085924677759136, 0.0)
    viewCenter118 = NXOpen.Point3d(16.75558329867064, 1.1085924677759433, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint118, viewCenter118)
    
    rotMatrix13 = NXOpen.Matrix3x3()
    
    rotMatrix13.Xx = 0.99824564710347674
    rotMatrix13.Xy = 0.027850244185338349
    rotMatrix13.Xz = -0.052249324759095224
    rotMatrix13.Yx = -0.034784600190926898
    rotMatrix13.Yy = 0.98997501590318948
    rotMatrix13.Yz = -0.13689229151798107
    rotMatrix13.Zx = 0.047913042363449621
    rotMatrix13.Zy = 0.13846960600183431
    rotMatrix13.Zz = 0.98920700997576028
    translation13 = NXOpen.Point3d(-7.1648800400868664, -1.5789074055394445, -2.5006520751611436)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix13, translation13, 6.6826480863576707)
    
    rotMatrix14 = NXOpen.Matrix3x3()
    
    rotMatrix14.Xx = -0.98834985812119436
    rotMatrix14.Xy = 0.0087677579717469912
    rotMatrix14.Xz = -0.15194632069242509
    rotMatrix14.Yx = -0.029015345062199365
    rotMatrix14.Yy = 0.96917532864573663
    rotMatrix14.Yz = 0.24465749956898902
    rotMatrix14.Zx = 0.14940772303578512
    rotMatrix14.Zy = 0.24621597991311867
    rotMatrix14.Zz = -0.95762989903860307
    translation14 = NXOpen.Point3d(-21.754311383585073, -2.7221709226707005, 4.3147773139908008)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix14, translation14, 6.6826480863576707)
    
    scCollector7 = workPart.ScCollectors.CreateCollector()
    
    seedEdges23 = [NXOpen.Edge.Null] * 1 
    edge15 = extrude1.FindObject("EDGE * 120 * 170 {(-14.4999999999998,4,-0)(-7.4999999999999,4,-0)(-0.5,4,-0) EXTRUDE(2)}")
    seedEdges23[0] = edge15
    edgeMultipleSeedTangentRule23 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges23, 0.5, True)
    
    rules24 = [None] * 1 
    rules24[0] = edgeMultipleSeedTangentRule23
    scCollector7.ReplaceRules(rules24, False)
    
    scCollector7.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    scCollector7.Destroy()
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder7)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression48)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression47)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder7.Destroy()
    
    workPart.Expressions.Delete(expression45)
    
    workPart.Expressions.Delete(expression46)
    
    theSession.UndoToMark(markId68, None)
    
    theSession.DeleteUndoMark(markId68, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId69 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder2 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin11 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal11 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane11 = workPart.Planes.CreatePlane(origin11, normal11, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.PlaneReference = plane11
    
    expression49 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression50 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder2 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder2.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId69, "Create Sketch Dialog")
    
    edge16 = extrude1.FindObject("EDGE * 170 BLEND(5) 13 {(-0.5,4,-0)(-0.1464466094067,3.8535533905933,-0)(-0,3.5,-0) EXTRUDE(2)}")
    point16 = workPart.Points.CreatePoint(edge16, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction3 = workPart.Directions.CreateDirection(edge15, NXOpen.Sense.Reverse, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face1 = extrude1.FindObject("FACE 170 {(-7.4999999999999,0,-0) EXTRUDE(2)}")
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction3, point16, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder2.Csystem = cartesianCoordinateSystem2
    
    origin12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal12 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane12 = workPart.Planes.CreatePlane(origin12, normal12, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane12.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom7 = [NXOpen.NXObject.Null] * 1 
    geom7[0] = face1
    plane12.SetGeometry(geom7)
    
    plane12.SetFlip(False)
    
    plane12.SetExpression(None)
    
    plane12.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane12.Evaluate()
    
    origin13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal13 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane13 = workPart.Planes.CreatePlane(origin13, normal13, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression51 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression52 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane13.SynchronizeToPlane(plane12)
    
    point17 = workPart.Points.CreatePoint(edge16, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane13.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom8 = [NXOpen.NXObject.Null] * 1 
    geom8[0] = face1
    plane13.SetGeometry(geom8)
    
    plane13.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane13.Evaluate()
    
    edgeBlend3 = feature5
    face2 = edgeBlend3.FindObject("FACE 13 {(-0.1464466094067,3.8535533905933,0.8159460858115) EXTRUDE(2)}")
    line7 = workPart.Lines.CreateFaceAxis(face2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    line7.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId70 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    objects5 = [NXOpen.TaggedObject.Null] * 1 
    objects5[0] = line7
    nErrs11 = theSession.UpdateManager.AddObjectsToDeleteList(objects5)
    
    theSession.DeleteUndoMark(markId70, None)
    
    markId71 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject7 = sketchInPlaceBuilder2.Commit()
    
    sketch3 = nXObject7
    feature6 = sketch3.Feature
    
    markId72 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs12 = theSession.UpdateManager.DoUpdate(markId72)
    
    sketch3.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId71, None)
    
    theSession.SetUndoMarkName(markId69, "Create Sketch")
    
    sketchInPlaceBuilder2.Destroy()
    
    sketchAlongPathBuilder2.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression50)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point17)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression49)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane11.DestroyPlane()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression52)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression51)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane13.DestroyPlane()
    
    scaleAboutPoint119 = NXOpen.Point3d(6.3744066897117673, -4.0780365778900016, 0.0)
    viewCenter119 = NXOpen.Point3d(-6.3744066897113987, 4.0780365778900318, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint119, viewCenter119)
    
    scaleAboutPoint120 = NXOpen.Point3d(7.968008362139658, -5.097545722362506, 0.0)
    viewCenter120 = NXOpen.Point3d(-7.9680083621392956, 5.0975457223625398, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint120, viewCenter120)
    
    scaleAboutPoint121 = NXOpen.Point3d(9.9600104526745294, -6.3719321529531365, 0.0)
    viewCenter121 = NXOpen.Point3d(-9.96001045267416, 6.3719321529531685, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint121, viewCenter121)
    
    scaleAboutPoint122 = NXOpen.Point3d(12.450013065843114, -7.9649151911914275, 0.0)
    viewCenter122 = NXOpen.Point3d(-12.450013065842745, 7.9649151911914604, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint122, viewCenter122)
    
    scaleAboutPoint123 = NXOpen.Point3d(9.9600104526745294, -6.3719321529531365, 0.0)
    viewCenter123 = NXOpen.Point3d(-9.96001045267416, 6.3719321529531685, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint123, viewCenter123)
    
    scaleAboutPoint124 = NXOpen.Point3d(7.9680083621396607, -5.0975457223625051, 0.0)
    viewCenter124 = NXOpen.Point3d(-7.9680083621392894, 5.0975457223625353, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint124, viewCenter124)
    
    scaleAboutPoint125 = NXOpen.Point3d(6.3744066897117619, -4.0780365778900007, 0.0)
    viewCenter125 = NXOpen.Point3d(-6.3744066897113907, 4.0780365778900309, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint125, viewCenter125)
    
    scaleAboutPoint126 = NXOpen.Point3d(5.0995253517694428, -3.1990811212962345, 0.0)
    viewCenter126 = NXOpen.Point3d(-5.0995253517690804, 3.1990811212962642, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint126, viewCenter126)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Line...
    # ----------------------------------------------
    markId73 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId74 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId74, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint11 = NXOpen.Point3d(0.0, 2.1712727421942928, -1.4791141972893971e-31)
    endPoint11 = NXOpen.Point3d(-2.8578838324886395, 0.52127274219427866, -1.6493413793947771e-16)
    line8 = workPart.Curves.CreateLine(startPoint11, endPoint11)
    
    theSession.ActiveSketch.AddGeometry(line8, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_1.Geometry = line8
    conGeom1_1.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    conGeom1_1.SplineDefiningPointIndex = 0
    conGeom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    edge17 = extrude1.FindObject("EDGE * 170 * 180 {(0,-3.5,-0)(0,0,-0)(0,3.5,-0) EXTRUDE(2)}")
    conGeom2_1.Geometry = edge17
    conGeom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_1.SplineDefiningPointIndex = 0
    help1 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help1.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help1.Point.X = 0.0
    help1.Point.Y = 2.1712727421942928
    help1.Point.Z = -1.4791141972893971e-31
    help1.Parameter = 0.0
    sketchHelpedGeometricConstraint1 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_1, conGeom2_1, help1)
    
    dimObject1_9 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_9.Geometry = line8
    dimObject1_9.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_9.AssocValue = 0
    dimObject1_9.HelpPoint.X = 0.0
    dimObject1_9.HelpPoint.Y = 0.0
    dimObject1_9.HelpPoint.Z = 0.0
    dimObject1_9.View = NXOpen.NXObject.Null
    dimObject2_8 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_8.Geometry = line8
    dimObject2_8.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_8.AssocValue = 0
    dimObject2_8.HelpPoint.X = 0.0
    dimObject2_8.HelpPoint.Y = 0.0
    dimObject2_8.HelpPoint.Z = 0.0
    dimObject2_8.View = NXOpen.NXObject.Null
    dimOrigin9 = NXOpen.Point3d(-0.99797503563311174, 0.59981620859621154, -5.7595116469074124e-17)
    sketchDimensionalConstraint9 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_9, dimObject2_8, dimOrigin9, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint7 = sketchDimensionalConstraint9
    dimension9 = sketchHelpedDimensionalConstraint7.AssociatedDimension
    
    expression53 = sketchHelpedDimensionalConstraint7.AssociatedExpression
    
    dimObject1_10 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_10.Geometry = line8
    dimObject1_10.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject1_10.AssocValue = 0
    dimObject1_10.HelpPoint.X = -2.8578838324886395
    dimObject1_10.HelpPoint.Y = 0.52127274219427866
    dimObject1_10.HelpPoint.Z = -1.6493413793947771e-16
    dimObject1_10.View = NXOpen.NXObject.Null
    dimObject2_9 = NXOpen.Sketch.DimensionGeometry()
    
    datumAxis2 = workPart.Datums.FindObject("SKETCH(4:1B) X axis")
    dimObject2_9.Geometry = datumAxis2
    dimObject2_9.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_9.AssocValue = 0
    dimObject2_9.HelpPoint.X = -29.075000000000003
    dimObject2_9.HelpPoint.Y = 3.4999999999999996
    dimObject2_9.HelpPoint.Z = -1.6779758526484384e-15
    dimObject2_9.View = NXOpen.NXObject.Null
    dimOrigin10 = NXOpen.Point3d(-1.0980449094116183, 2.5891152868448613, -6.3370347140713393e-17)
    sketchDimensionalConstraint10 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.AngularDim, dimObject1_10, dimObject2_9, dimOrigin10, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension10 = sketchDimensionalConstraint10.AssociatedDimension
    
    expression54 = sketchDimensionalConstraint10.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   Dialog Begin Line
    # ----------------------------------------------
    markId75 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId75, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint12 = NXOpen.Point3d(-2.8578838324886395, -0.74274174453100494, -1.6493413793947771e-16)
    endPoint12 = NXOpen.Point3d(1.4432899320127035e-15, -2.0603830776589631, -6.7792734042430702e-32)
    line9 = workPart.Curves.CreateLine(startPoint12, endPoint12)
    
    theSession.ActiveSketch.AddGeometry(line9, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    conGeom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_2.Geometry = line9
    conGeom1_2.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    conGeom1_2.SplineDefiningPointIndex = 0
    conGeom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_2.Geometry = edge17
    conGeom2_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_2.SplineDefiningPointIndex = 0
    help2 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help2.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help2.Point.X = 0.0
    help2.Point.Y = -2.0603830776589658
    help2.Point.Z = -1.4791141972893971e-31
    help2.Parameter = 0.0
    sketchHelpedGeometricConstraint2 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_2, conGeom2_2, help2)
    
    dimObject1_11 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_11.Geometry = line9
    dimObject1_11.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_11.AssocValue = 0
    dimObject1_11.HelpPoint.X = 0.0
    dimObject1_11.HelpPoint.Y = 0.0
    dimObject1_11.HelpPoint.Z = 0.0
    dimObject1_11.View = NXOpen.NXObject.Null
    dimObject2_10 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_10.Geometry = line9
    dimObject2_10.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_10.AssocValue = 0
    dimObject2_10.HelpPoint.X = 0.0
    dimObject2_10.HelpPoint.Y = 0.0
    dimObject2_10.HelpPoint.Z = 0.0
    dimObject2_10.View = NXOpen.NXObject.Null
    dimOrigin11 = NXOpen.Point3d(-1.0680535925363643, -0.61881760814432185, -6.1639488825810391e-17)
    sketchDimensionalConstraint11 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_11, dimObject2_10, dimOrigin11, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint8 = sketchDimensionalConstraint11
    dimension11 = sketchHelpedDimensionalConstraint8.AssociatedDimension
    
    expression55 = sketchHelpedDimensionalConstraint8.AssociatedExpression
    
    dimObject1_12 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_12.Geometry = line9
    dimObject1_12.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject1_12.AssocValue = 0
    dimObject1_12.HelpPoint.X = 1.4432899320127035e-15
    dimObject1_12.HelpPoint.Y = -2.0603830776589631
    dimObject1_12.HelpPoint.Z = -6.7792734042430702e-32
    dimObject1_12.View = NXOpen.NXObject.Null
    dimObject2_11 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_11.Geometry = datumAxis2
    dimObject2_11.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_11.AssocValue = 0
    dimObject2_11.HelpPoint.X = -29.075000000000003
    dimObject2_11.HelpPoint.Y = 3.4999999999999996
    dimObject2_11.HelpPoint.Z = -1.6779758526484384e-15
    dimObject2_11.View = NXOpen.NXObject.Null
    dimOrigin12 = NXOpen.Point3d(-14.416710543571487, -7.2396480969163619, -8.3201692748873972e-16)
    sketchDimensionalConstraint12 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.AngularDim, dimObject1_12, dimObject2_11, dimOrigin12, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension12 = sketchDimensionalConstraint12.AssociatedDimension
    
    expression56 = sketchDimensionalConstraint12.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   Dialog Begin Line
    # ----------------------------------------------
    markId76 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId76, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint13 = NXOpen.Point3d(-2.8578838324886395, 0.52127274219427866, -1.6493413793947771e-16)
    endPoint13 = NXOpen.Point3d(-2.8578838324886369, -0.74274174453100494, -1.6493413793947754e-16)
    line10 = workPart.Curves.CreateLine(startPoint13, endPoint13)
    
    theSession.ActiveSketch.AddGeometry(line10, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_12 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_12.Geometry = line10
    geom1_12.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_12.SplineDefiningPointIndex = 0
    geom2_12 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_12.Geometry = line8
    geom2_12.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_12.SplineDefiningPointIndex = 0
    sketchGeometricConstraint15 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_12, geom2_12)
    
    geom9 = NXOpen.Sketch.ConstraintGeometry()
    
    geom9.Geometry = line10
    geom9.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom9.SplineDefiningPointIndex = 0
    sketchGeometricConstraint16 = theSession.ActiveSketch.CreateVerticalConstraint(geom9)
    
    geom1_13 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_13.Geometry = line10
    geom1_13.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_13.SplineDefiningPointIndex = 0
    geom2_13 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_13.Geometry = line9
    geom2_13.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_13.SplineDefiningPointIndex = 0
    sketchGeometricConstraint17 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_13, geom2_13)
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   Dialog Begin Line
    # ----------------------------------------------
    markId77 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId77, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint14 = NXOpen.Point3d(0.0, 2.1712727421942928, -1.4791141972893971e-31)
    endPoint14 = NXOpen.Point3d(8.3266726846886741e-15, -2.0603830776589622, 3.3280069439011436e-31)
    line11 = workPart.Curves.CreateLine(startPoint14, endPoint14)
    
    theSession.ActiveSketch.AddGeometry(line11, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_14 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_14.Geometry = line11
    geom1_14.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_14.SplineDefiningPointIndex = 0
    geom2_14 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_14.Geometry = line8
    geom2_14.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_14.SplineDefiningPointIndex = 0
    sketchGeometricConstraint18 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_14, geom2_14)
    
    geom10 = NXOpen.Sketch.ConstraintGeometry()
    
    geom10.Geometry = line11
    geom10.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom10.SplineDefiningPointIndex = 0
    sketchGeometricConstraint19 = theSession.ActiveSketch.CreateVerticalConstraint(geom10)
    
    geom1_15 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_15.Geometry = line11
    geom1_15.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_15.SplineDefiningPointIndex = 0
    geom2_15 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_15.Geometry = line9
    geom2_15.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom2_15.SplineDefiningPointIndex = 0
    sketchGeometricConstraint20 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_15, geom2_15)
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   Dialog Begin Line
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Sketch Constraint->Dimension->Rapid...
    # ----------------------------------------------
    markId78 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder6 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines21 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBefore(lines21)
    
    lines22 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAfter(lines22)
    
    lines23 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAbove(lines23)
    
    lines24 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBelow(lines24)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder6.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines25 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBefore(lines25)
    
    lines26 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAfter(lines26)
    
    lines27 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAbove(lines27)
    
    lines28 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBelow(lines28)
    
    theSession.SetUndoMarkName(markId78, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder6.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits125 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits126 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits127 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits128 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits129 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits130 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits131 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits132 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits133 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits134 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder6.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits135 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits136 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits137 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits138 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits139 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits140 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits141 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits142 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits143 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits144 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    point18 = NXOpen.Point3d(-2.8578838324886391, 0.24548925531496524, -1.6493413793947768e-16)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(line10, workPart.ModelingViews.WorkView, point18)
    
    point1_11 = NXOpen.Point3d(-2.8578838324886395, 0.52127274219427866, -1.6493413793947771e-16)
    point2_11 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line10, workPart.ModelingViews.WorkView, point1_11, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_11)
    
    point1_12 = NXOpen.Point3d(-2.8578838324886369, -0.74274174453100494, -1.6493413793947754e-16)
    point2_12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder6.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line10, workPart.ModelingViews.WorkView, point1_12, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_12)
    
    dimensionlinearunits145 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits146 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits147 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits148 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits149 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits150 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin5 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin5.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin5.View = NXOpen.View.Null
    assocOrigin5.ViewOfGeometry = workPart.ModelingViews.WorkView
    point19 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin5.PointOnGeometry = point19
    assocOrigin5.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin5.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin5.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.DimensionLine = 0
    assocOrigin5.AssociatedView = NXOpen.View.Null
    assocOrigin5.AssociatedPoint = NXOpen.Point.Null
    assocOrigin5.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin5.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin5.XOffsetFactor = 0.0
    assocOrigin5.YOffsetFactor = 0.0
    assocOrigin5.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder6.Origin.SetAssociativeOrigin(assocOrigin5)
    
    point20 = NXOpen.Point3d(-5.0499802284576489, -0.23595661640486743, -2.9144436387631917e-16)
    sketchRapidDimensionBuilder6.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point20)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.TextCentered = True
    
    markId79 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject8 = sketchRapidDimensionBuilder6.Commit()
    
    theSession.DeleteUndoMark(markId79, None)
    
    theSession.SetUndoMarkName(markId78, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId78, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder6.Destroy()
    
    markId80 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder7 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines29 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBefore(lines29)
    
    lines30 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAfter(lines30)
    
    lines31 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAbove(lines31)
    
    lines32 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBelow(lines32)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder7.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId80, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder7.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits151 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits152 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits153 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits154 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits155 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits156 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits157 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits158 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits159 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits160 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder7.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits161 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits162 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits163 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits164 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits165 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits166 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits167 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits168 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits169 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits170 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    expression57 = workPart.Expressions.FindObject("p14")
    expression57.SetFormula("1")
    
    theSession.SetUndoMarkVisibility(markId80, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId81 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId81, None)
    
    markId82 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId80, "Edit Driving Value")
    
    point21 = NXOpen.Point3d(8.5362610708893742e-48, 1.4110950500050841, -1.4791141972893971e-31)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(line11, workPart.ModelingViews.WorkView, point21)
    
    point1_13 = NXOpen.Point3d(0.0, 2.1712727421942928, -1.4791141972893971e-31)
    point2_13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line11, workPart.ModelingViews.WorkView, point1_13, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_13)
    
    point1_14 = NXOpen.Point3d(0.0, -1.7963685909336697, -1.4791141972893971e-31)
    point2_14 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line11, workPart.ModelingViews.WorkView, point1_14, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_14)
    
    dimensionlinearunits171 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits172 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits173 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits174 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits175 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits176 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin6 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin6.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin6.View = NXOpen.View.Null
    assocOrigin6.ViewOfGeometry = workPart.ModelingViews.WorkView
    point22 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin6.PointOnGeometry = point22
    assocOrigin6.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin6.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin6.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.DimensionLine = 0
    assocOrigin6.AssociatedView = NXOpen.View.Null
    assocOrigin6.AssociatedPoint = NXOpen.Point.Null
    assocOrigin6.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin6.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin6.XOffsetFactor = 0.0
    assocOrigin6.YOffsetFactor = 0.0
    assocOrigin6.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder7.Origin.SetAssociativeOrigin(assocOrigin6)
    
    point23 = NXOpen.Point3d(2.982564052341643, 0.77761363984741028, 1.7212968044046582e-16)
    sketchRapidDimensionBuilder7.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point23)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.TextCentered = False
    
    markId83 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject9 = sketchRapidDimensionBuilder7.Commit()
    
    theSession.DeleteUndoMark(markId83, None)
    
    theSession.SetUndoMarkName(markId82, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId82, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder7.Destroy()
    
    markId84 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder8 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines33 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBefore(lines33)
    
    lines34 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAfter(lines34)
    
    lines35 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAbove(lines35)
    
    lines36 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBelow(lines36)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder8.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId84, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder8.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits177 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits178 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits179 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits180 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits181 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits182 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits183 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits184 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits185 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits186 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder8.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits187 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits188 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits189 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits190 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits191 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits192 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits193 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits194 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits195 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits196 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    expression58 = workPart.Expressions.FindObject("p15")
    expression58.SetFormula("3")
    
    theSession.SetUndoMarkVisibility(markId84, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId85 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId85, None)
    
    markId86 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId84, "Edit Driving Value")
    
    point1_15 = NXOpen.Point3d(0.0, 2.1712727421942928, -1.4791141972893971e-31)
    point2_15 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line8, workPart.ModelingViews.WorkView, point1_15, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_15)
    
    edge18 = extrude1.FindObject("EDGE * 160 * 170 {(-14.9999999999998,-3.5,-0)(-14.9999999999998,0,-0)(-14.9999999999998,3.5,-0) EXTRUDE(2)}")
    point1_16 = NXOpen.Point3d(-14.999999999999799, -2.2204460492503131e-16, -8.6736173798840355e-16)
    point2_16 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, edge18, workPart.ModelingViews.WorkView, point1_16, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_16)
    
    point1_17 = NXOpen.Point3d(0.0, 2.1712727421942928, -1.4791141972893971e-31)
    point2_17 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line8, workPart.ModelingViews.WorkView, point1_17, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_17)
    
    point1_18 = NXOpen.Point3d(-14.999999999999799, -2.2204460492503131e-16, -8.6736173798840355e-16)
    point2_18 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, edge18, workPart.ModelingViews.WorkView, point1_18, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_18)
    
    dimensionlinearunits197 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits198 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits199 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits200 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits201 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits202 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    point1_19 = NXOpen.Point3d(0.0, 2.1712727421942928, -1.4791141972893971e-31)
    point2_19 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line8, workPart.ModelingViews.WorkView, point1_19, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_19)
    
    point1_20 = NXOpen.Point3d(-14.999999999999799, -2.2204460492503131e-16, -8.6736173798840355e-16)
    point2_20 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Mid, edge18, workPart.ModelingViews.WorkView, point1_20, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_20)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin7 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin7.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin7.View = NXOpen.View.Null
    assocOrigin7.ViewOfGeometry = workPart.ModelingViews.WorkView
    point24 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin7.PointOnGeometry = point24
    assocOrigin7.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin7.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin7.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.DimensionLine = 0
    assocOrigin7.AssociatedView = NXOpen.View.Null
    assocOrigin7.AssociatedPoint = NXOpen.Point.Null
    assocOrigin7.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin7.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin7.XOffsetFactor = 0.0
    assocOrigin7.YOffsetFactor = 0.0
    assocOrigin7.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder8.Origin.SetAssociativeOrigin(assocOrigin7)
    
    point25 = NXOpen.Point3d(6.0232748210984735, 1.3350772807861633, 3.4761512308404383e-16)
    sketchRapidDimensionBuilder8.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point25)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.TextCentered = False
    
    markId87 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject10 = sketchRapidDimensionBuilder8.Commit()
    
    theSession.DeleteUndoMark(markId87, None)
    
    theSession.SetUndoMarkName(markId86, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId86, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder8.Destroy()
    
    markId88 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder9 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines37 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBefore(lines37)
    
    lines38 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAfter(lines38)
    
    lines39 = []
    sketchRapidDimensionBuilder9.AppendedText.SetAbove(lines39)
    
    lines40 = []
    sketchRapidDimensionBuilder9.AppendedText.SetBelow(lines40)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder9.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId88, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder9.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits203 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits204 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits205 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits206 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits207 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits208 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits209 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits210 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits211 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits212 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder9.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits213 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits214 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits215 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits216 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits217 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits218 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits219 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits220 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits221 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits222 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    expression59 = workPart.Expressions.FindObject("p16")
    expression59.SetFormula("1.5")
    
    theSession.SetUndoMarkVisibility(markId88, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId89 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId89, None)
    
    markId90 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId88, "Edit Driving Value")
    
    point1_21 = NXOpen.Point3d(-1.9260304812349811, 0.38800578319155621, -1.1115503487453663e-16)
    point2_21 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line10, workPart.ModelingViews.WorkView, point1_21, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_21)
    
    point26 = NXOpen.Point3d(8.5362610708893742e-48, 0.92964917828525184, -1.4791141972893971e-31)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(line11, workPart.ModelingViews.WorkView, point26)
    
    point1_22 = NXOpen.Point3d(8.5362610708893742e-48, 0.92964917828525184, -1.4791141972893971e-31)
    point2_22 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line11, workPart.ModelingViews.WorkView, point1_22, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_22)
    
    point1_23 = NXOpen.Point3d(-1.9260304812349811, 0.38800578319155621, -1.1115503487453663e-16)
    point2_23 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder9.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line10, workPart.ModelingViews.WorkView, point1_23, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_23)
    
    dimensionlinearunits223 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits224 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits225 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits226 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits227 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits228 = sketchRapidDimensionBuilder9.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin8 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin8.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin8.View = NXOpen.View.Null
    assocOrigin8.ViewOfGeometry = workPart.ModelingViews.WorkView
    point27 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin8.PointOnGeometry = point27
    assocOrigin8.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin8.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin8.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.DimensionLine = 0
    assocOrigin8.AssociatedView = NXOpen.View.Null
    assocOrigin8.AssociatedPoint = NXOpen.Point.Null
    assocOrigin8.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin8.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin8.XOffsetFactor = 0.0
    assocOrigin8.YOffsetFactor = 0.0
    assocOrigin8.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder9.Origin.SetAssociativeOrigin(assocOrigin8)
    
    point28 = NXOpen.Point3d(-1.2997702803242257, -5.1010938464157967, -7.5012317949239756e-17)
    sketchRapidDimensionBuilder9.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point28)
    
    sketchRapidDimensionBuilder9.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder9.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder9.Style.DimensionStyle.TextCentered = False
    
    markId91 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject11 = sketchRapidDimensionBuilder9.Commit()
    
    theSession.DeleteUndoMark(markId91, None)
    
    theSession.SetUndoMarkName(markId90, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId90, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder9.Destroy()
    
    markId92 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder10 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines41 = []
    sketchRapidDimensionBuilder10.AppendedText.SetBefore(lines41)
    
    lines42 = []
    sketchRapidDimensionBuilder10.AppendedText.SetAfter(lines42)
    
    lines43 = []
    sketchRapidDimensionBuilder10.AppendedText.SetAbove(lines43)
    
    lines44 = []
    sketchRapidDimensionBuilder10.AppendedText.SetBelow(lines44)
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder10.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId92, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder10.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits229 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits230 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits231 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits232 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits233 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits234 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits235 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits236 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits237 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits238 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder10.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder10.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder10.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits239 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits240 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits241 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits242 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits243 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits244 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits245 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits246 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits247 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits248 = sketchRapidDimensionBuilder10.Style.UnitsStyle.DimensionLinearUnits
    
    expression60 = workPart.Expressions.FindObject("p17")
    expression60.SetFormula("2")
    
    theSession.SetUndoMarkVisibility(markId92, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId93 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId93, None)
    
    markId94 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId92, "Edit Driving Value")
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketchRapidDimensionBuilder10.Destroy()
    
    theSession.UndoToMark(markId94, None)
    
    theSession.DeleteUndoMark(markId94, None)
    
    sketchRapidDimensionBuilder10.Destroy()
    
    sketch4 = theSession.ActiveSketch
    
    markId95 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId96 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder3 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section3 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder3.Section = section3
    
    extrudeBuilder3.AllowSelfIntersectingSection(True)
    
    expression61 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder3.DistanceTolerance = 0.01
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies4 = [NXOpen.Body.Null] * 1 
    targetBodies4[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies4)
    
    extrudeBuilder3.Limits.StartExtend.Value.SetFormula("4")
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("4")
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies5 = [NXOpen.Body.Null] * 1 
    targetBodies5[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies5)
    
    extrudeBuilder3.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder3.Offset.EndOffset.SetFormula("5")
    
    extrudeBuilder3.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("4")
    
    smartVolumeProfileBuilder3 = extrudeBuilder3.SmartVolumeProfile
    
    smartVolumeProfileBuilder3.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder3.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId96, "Extrude Dialog")
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    section3.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId97 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId98 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features2 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature2 = feature6
    features2[0] = sketchFeature2
    curveFeatureRule2 = workPart.ScRuleFactory.CreateRuleCurveFeature(features2)
    
    section3.AllowSelfIntersection(True)
    
    rules25 = [None] * 1 
    rules25[0] = curveFeatureRule2
    helpPoint2 = NXOpen.Point3d(-1.6208399534039775, 0.56420761658891194, 4.163336342344337e-17)
    section3.AddToSection(rules25, line8, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId98, None)
    
    direction4 = workPart.Directions.CreateDirection(sketch4, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder3.Direction = direction4
    
    targetBodies6 = [NXOpen.Body.Null] * 1 
    body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
    targetBodies6[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies6)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies7 = [NXOpen.Body.Null] * 1 
    targetBodies7[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies7)
    
    expression62 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId97, None)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies8 = [NXOpen.Body.Null] * 1 
    targetBodies8[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies8)
    
    direction5 = extrudeBuilder3.Direction
    
    success1 = direction5.ReverseDirection()
    
    extrudeBuilder3.Direction = direction5
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies9 = [NXOpen.Body.Null] * 1 
    targetBodies9[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies9)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies10 = [NXOpen.Body.Null] * 1 
    targetBodies10[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies10)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies11 = [NXOpen.Body.Null] * 1 
    targetBodies11[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies11)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies12 = [NXOpen.Body.Null] * 1 
    targetBodies12[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies12)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies13 = [NXOpen.Body.Null] * 1 
    targetBodies13[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies13)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies14 = [NXOpen.Body.Null] * 1 
    targetBodies14[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies14)
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("8")
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies15 = [NXOpen.Body.Null] * 1 
    targetBodies15[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies15)
    
    markId99 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder3.ParentFeatureInternal = False
    
    feature7 = extrudeBuilder3.CommitFeature()
    
    theSession.DeleteUndoMark(markId99, None)
    
    theSession.SetUndoMarkName(markId96, "Extrude")
    
    expression63 = extrudeBuilder3.Limits.StartExtend.Value
    expression64 = extrudeBuilder3.Limits.EndExtend.Value
    extrudeBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression61)
    
    workPart.Expressions.Delete(expression62)
    
    markId100 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder4 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section4 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder4.Section = section4
    
    extrudeBuilder4.AllowSelfIntersectingSection(True)
    
    expression65 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder4.DistanceTolerance = 0.01
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies16 = [NXOpen.Body.Null] * 1 
    targetBodies16[0] = NXOpen.Body.Null
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies16)
    
    extrudeBuilder4.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder4.Limits.EndExtend.Value.SetFormula("8")
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies17 = [NXOpen.Body.Null] * 1 
    targetBodies17[0] = NXOpen.Body.Null
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies17)
    
    extrudeBuilder4.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder4.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder4.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder4.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder4 = extrudeBuilder4.SmartVolumeProfile
    
    smartVolumeProfileBuilder4.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder4.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId100, "Extrude Dialog")
    
    section4.DistanceTolerance = 0.01
    
    section4.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   Dialog Begin Extrude
    # ----------------------------------------------
    section4.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    extrudeBuilder4.Destroy()
    
    section4.Destroy()
    
    workPart.Expressions.Delete(expression65)
    
    theSession.UndoToMark(markId100, None)
    
    theSession.DeleteUndoMark(markId100, None)
    
    markId101 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects6 = [NXOpen.DisplayableObject.Null] * 5 
    objects6[0] = line10
    objects6[1] = line8
    objects6[2] = line9
    objects6[3] = sketch4
    objects6[4] = line11
    theSession.DisplayManager.BlankObjects(objects6)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    rotMatrix15 = NXOpen.Matrix3x3()
    
    rotMatrix15.Xx = 0.33961976015182938
    rotMatrix15.Xy = 0.91997585303860896
    rotMatrix15.Xz = -0.19571113494203854
    rotMatrix15.Yx = -0.25788660661182378
    rotMatrix15.Yy = 0.29118454294091811
    rotMatrix15.Yz = 0.92125244101849157
    rotMatrix15.Zx = 0.90451805766643312
    rotMatrix15.Zy = -0.2624042525916353
    rotMatrix15.Zz = 0.33614147553845941
    translation15 = NXOpen.Point3d(-11.65844064414877, -6.5427615191893143, 5.954770578861508)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix15, translation15, 6.6826480863576707)
    
    rotMatrix16 = NXOpen.Matrix3x3()
    
    rotMatrix16.Xx = 0.99876139797916819
    rotMatrix16.Xy = 0.0075818041468196165
    rotMatrix16.Xz = 0.049175056203150477
    rotMatrix16.Yx = -0.049179942219934401
    rotMatrix16.Yy = 0.30039738666729127
    rotMatrix16.Yz = 0.95254540226002338
    rotMatrix16.Zx = -0.0075500456917548661
    rotMatrix16.Zy = -0.95378400402258068
    rotMatrix16.Zz = 0.30039818654697542
    translation16 = NXOpen.Point3d(-7.4764186281356544, -5.0747755169581064, -0.77458671013004743)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix16, translation16, 6.6826480863576707)
    
    rotMatrix17 = NXOpen.Matrix3x3()
    
    rotMatrix17.Xx = 0.99737519842760414
    rotMatrix17.Xy = 0.063943863048725916
    rotMatrix17.Xz = 0.033969043847356488
    rotMatrix17.Yx = -0.034001882406173016
    rotMatrix17.Yy = -0.00057491143836817249
    rotMatrix17.Yz = 0.9994216034635609
    rotMatrix17.Zx = 0.063926407331670265
    rotMatrix17.Zy = -0.99795333150165133
    rotMatrix17.Zz = 0.0016008093020584504
    translation17 = NXOpen.Point3d(-7.4395278903807478, -5.1067143753747555, 0.69067846266631072)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix17, translation17, 6.6826480863576707)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch...
    # ----------------------------------------------
    markId102 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder3 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin14 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal14 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane14 = workPart.Planes.CreatePlane(origin14, normal14, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder3.PlaneReference = plane14
    
    expression66 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression67 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder3 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    sketchAlongPathBuilder3.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId102, "Create Sketch Dialog")
    
    scalar1 = workPart.Scalars.CreateScalar(1.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge19 = extrude1.FindObject("EDGE * 130 BLEND(3) 8 {(-4.5206593815027,-4,3.1428558026597)(-8.6792572963439,-4,5.7018642650841)(-13.1963675513023,-4,3.8476323829746) EXTRUDE(2)}")
    point29 = workPart.Points.CreatePoint(edge19, scalar1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge20 = extrude1.FindObject("EDGE * 130 * 170 {(-14.4999999999998,-4,-0)(-7.4999999999999,-4,-0)(-0.5,-4,-0) EXTRUDE(2)}")
    direction6 = workPart.Directions.CreateDirection(edge20, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face3 = extrude1.FindObject("FACE 130 {(-7.5,-4,2.8769308262358) EXTRUDE(2)}")
    xform3 = workPart.Xforms.CreateXformByPlaneXDirPoint(face3, direction6, point29, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem3 = workPart.CoordinateSystems.CreateCoordinateSystem(xform3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder3.Csystem = cartesianCoordinateSystem3
    
    origin15 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal15 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane15 = workPart.Planes.CreatePlane(origin15, normal15, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane15.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom11 = [NXOpen.NXObject.Null] * 1 
    geom11[0] = face3
    plane15.SetGeometry(geom11)
    
    plane15.SetFlip(False)
    
    plane15.SetExpression(None)
    
    plane15.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane15.Evaluate()
    
    origin16 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal16 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane16 = workPart.Planes.CreatePlane(origin16, normal16, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression68 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression69 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane16.SynchronizeToPlane(plane15)
    
    scalar2 = workPart.Scalars.CreateScalar(100.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point30 = workPart.Points.CreatePoint(edge19, scalar2, NXOpen.PointCollection.PointOnCurveLocationOption.PercentParameter, NXOpen.Point.Null, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane16.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom12 = [NXOpen.NXObject.Null] * 1 
    geom12[0] = face3
    plane16.SetGeometry(geom12)
    
    plane16.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane16.Evaluate()
    
    markId103 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.DeleteUndoMark(markId103, None)
    
    markId104 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject12 = sketchInPlaceBuilder3.Commit()
    
    sketch5 = nXObject12
    feature8 = sketch5.Feature
    
    markId105 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs13 = theSession.UpdateManager.DoUpdate(markId105)
    
    sketch5.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId104, None)
    
    theSession.SetUndoMarkName(markId102, "Create Sketch")
    
    sketchInPlaceBuilder3.Destroy()
    
    sketchAlongPathBuilder3.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression67)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.Points.DeletePoint(point30)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression66)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane14.DestroyPlane()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression69)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression68)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane16.DestroyPlane()
    
    scaleAboutPoint127 = NXOpen.Point3d(17.064405486122499, -0.71266658642736536, 0.0)
    viewCenter127 = NXOpen.Point3d(-17.06440548612213, 0.71266658642739578, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint127, viewCenter127)
    
    scaleAboutPoint128 = NXOpen.Point3d(12.542931921122113, -1.1719406087916802, 0.0)
    viewCenter128 = NXOpen.Point3d(-12.542931921121745, 1.171940608791707, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint128, viewCenter128)
    
    scaleAboutPoint129 = NXOpen.Point3d(8.4633116397066974, -1.1402665382837966, 0.0)
    viewCenter129 = NXOpen.Point3d(-8.4633116397063262, 1.1402665382838246, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint129, viewCenter129)
    
    scaleAboutPoint130 = NXOpen.Point3d(6.3652212092644866, -1.0135702562522628, 0.0)
    viewCenter130 = NXOpen.Point3d(-6.3652212092641118, 1.0135702562522904, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint130, viewCenter130)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Curve->Circle...
    # ----------------------------------------------
    markId106 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId107 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId107, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix2 = theSession.ActiveSketch.Orientation
    
    center5 = NXOpen.Point3d(-12.496367551302281, -4.0, 0.64763238297463976)
    arc2 = workPart.Curves.CreateArc(center5, nXMatrix2, 0.40629033100807249, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_13 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_13.Geometry = arc2
    dimObject1_13.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_13.AssocValue = 0
    dimObject1_13.HelpPoint.X = 0.0
    dimObject1_13.HelpPoint.Y = 0.0
    dimObject1_13.HelpPoint.Z = 0.0
    dimObject1_13.View = NXOpen.NXObject.Null
    dimOrigin13 = NXOpen.Point3d(-12.496367551302281, -4.0, 0.83151158536875358)
    sketchDimensionalConstraint13 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_13, dimOrigin13, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension13 = sketchDimensionalConstraint13.AssociatedDimension
    
    expression70 = sketchDimensionalConstraint13.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    markId108 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId108, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix3 = theSession.ActiveSketch.Orientation
    
    center6 = NXOpen.Point3d(-4.811924347160204, -4.0, 0.64763238297463976)
    arc3 = workPart.Curves.CreateArc(center6, nXMatrix3, 0.42354727098514655, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_14 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_14.Geometry = arc3
    dimObject1_14.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_14.AssocValue = 0
    dimObject1_14.HelpPoint.X = 0.0
    dimObject1_14.HelpPoint.Y = 0.0
    dimObject1_14.HelpPoint.Z = 0.0
    dimObject1_14.View = NXOpen.NXObject.Null
    dimOrigin14 = NXOpen.Point3d(-4.811924347160204, -4.0, 0.83151158536875358)
    sketchDimensionalConstraint14 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_14, dimOrigin14, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension14 = sketchDimensionalConstraint14.AssociatedDimension
    
    expression71 = sketchDimensionalConstraint14.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Sketch Constraint->Dimension->Rapid...
    # ----------------------------------------------
    markId109 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder11 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines45 = []
    sketchRapidDimensionBuilder11.AppendedText.SetBefore(lines45)
    
    lines46 = []
    sketchRapidDimensionBuilder11.AppendedText.SetAfter(lines46)
    
    lines47 = []
    sketchRapidDimensionBuilder11.AppendedText.SetAbove(lines47)
    
    lines48 = []
    sketchRapidDimensionBuilder11.AppendedText.SetBelow(lines48)
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder11.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines49 = []
    sketchRapidDimensionBuilder11.AppendedText.SetBefore(lines49)
    
    lines50 = []
    sketchRapidDimensionBuilder11.AppendedText.SetAfter(lines50)
    
    lines51 = []
    sketchRapidDimensionBuilder11.AppendedText.SetAbove(lines51)
    
    lines52 = []
    sketchRapidDimensionBuilder11.AppendedText.SetBelow(lines52)
    
    theSession.SetUndoMarkName(markId109, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder11.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits249 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits250 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits251 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits252 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits253 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits254 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits255 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits256 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits257 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits258 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder11.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder11.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits259 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits260 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits261 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits262 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits263 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits264 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits265 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits266 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits267 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits268 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    point1_24 = NXOpen.Point3d(-12.23086724149057, -4.0, 0.9551733047404023)
    point2_24 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder11.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_24, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_24)
    
    point1_25 = NXOpen.Point3d(-12.23086724149057, -4.0, 0.9551733047404023)
    point2_25 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder11.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_25, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_25)
    
    point1_26 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_26 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder11.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_26, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_26)
    
    dimensionlinearunits269 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits270 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits271 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits272 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits273 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits274 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    point1_27 = NXOpen.Point3d(-4.6573307316315837, -4.0, 1.0419585231134265)
    point2_27 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder11.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc3, workPart.ModelingViews.WorkView, point1_27, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_27)
    
    point1_28 = NXOpen.Point3d(-12.23086724149057, -4.0, 0.9551733047404023)
    point2_28 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder11.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_28, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_28)
    
    point1_29 = NXOpen.Point3d(-4.6573307316315837, -4.0, 1.0419585231134265)
    point2_29 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder11.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc3, workPart.ModelingViews.WorkView, point1_29, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_29)
    
    point1_30 = NXOpen.Point3d(-12.23086724149057, -4.0, 0.9551733047404023)
    point2_30 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder11.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_30, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_30)
    
    point1_31 = NXOpen.Point3d(-4.6573307316315837, -4.0, 1.0419585231134265)
    point2_31 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder11.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc3, workPart.ModelingViews.WorkView, point1_31, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_31)
    
    dimensionlinearunits275 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits276 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits277 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits278 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits279 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits280 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits281 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits282 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits283 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits284 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits285 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits286 = sketchRapidDimensionBuilder11.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin9 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin9.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin9.View = NXOpen.View.Null
    assocOrigin9.ViewOfGeometry = workPart.ModelingViews.WorkView
    point31 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin9.PointOnGeometry = point31
    assocOrigin9.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin9.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin9.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin9.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin9.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin9.DimensionLine = 0
    assocOrigin9.AssociatedView = NXOpen.View.Null
    assocOrigin9.AssociatedPoint = NXOpen.Point.Null
    assocOrigin9.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin9.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin9.XOffsetFactor = 0.0
    assocOrigin9.YOffsetFactor = 0.0
    assocOrigin9.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder11.Origin.SetAssociativeOrigin(assocOrigin9)
    
    point32 = NXOpen.Point3d(-8.8662053721693113, -4.0, -1.2738114255860662)
    sketchRapidDimensionBuilder11.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point32)
    
    sketchRapidDimensionBuilder11.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder11.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder11.Style.DimensionStyle.TextCentered = True
    
    markId110 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject13 = sketchRapidDimensionBuilder11.Commit()
    
    theSession.DeleteUndoMark(markId110, None)
    
    theSession.SetUndoMarkName(markId109, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId109, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder11.Destroy()
    
    markId111 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder12 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines53 = []
    sketchRapidDimensionBuilder12.AppendedText.SetBefore(lines53)
    
    lines54 = []
    sketchRapidDimensionBuilder12.AppendedText.SetAfter(lines54)
    
    lines55 = []
    sketchRapidDimensionBuilder12.AppendedText.SetAbove(lines55)
    
    lines56 = []
    sketchRapidDimensionBuilder12.AppendedText.SetBelow(lines56)
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder12.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder12.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder12.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder12.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId111, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder12.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits287 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits288 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits289 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits290 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits291 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits292 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits293 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits294 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits295 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits296 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder12.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder12.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder12.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits297 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits298 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits299 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits300 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits301 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits302 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits303 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits304 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits305 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits306 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    expression72 = workPart.Expressions.FindObject("p20")
    expression72.SetFormula("7")
    
    theSession.SetUndoMarkVisibility(markId111, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId112 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.90889022800300456)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId112, None)
    
    markId113 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId111, "Edit Driving Value")
    
    horizontalDimension1 = nXObject13
    point33 = NXOpen.Point3d(-8.3472574009681448, -4.0, -1.0745760439829031)
    sketchRapidDimensionBuilder12.FirstAssociativity.SetValue(horizontalDimension1, workPart.ModelingViews.WorkView, point33)
    
    sketchRapidDimensionBuilder12.FirstAssociativity.Value = NXOpen.TaggedObject.Null
    
    expression72.SetFormula("8")
    
    theSession.SetUndoMarkVisibility(markId113, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId114 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(1.1428571428571428)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId114, None)
    
    markId115 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId113, "Edit Driving Value")
    
    point1_32 = NXOpen.Point3d(-12.303402589591892, -4.0, 0.91176228815702398)
    point2_32 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder12.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_32, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_32)
    
    point1_33 = NXOpen.Point3d(-12.303402589591892, -4.0, 0.91176228815702398)
    point2_33 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder12.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_33, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_33)
    
    point1_34 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_34 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder12.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_34, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_34)
    
    dimensionlinearunits307 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits308 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits309 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits310 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits311 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits312 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    edge21 = extrude1.FindObject("EDGE * 160 BLEND(3) 4 {(-14.9999999999998,-3.5,-0)(-14.9999999999999,-3.5,1.75)(-15,-3.5,3.5) EXTRUDE(2)}")
    point34 = NXOpen.Point3d(-14.999999999999854, -3.5, 1.0614544448191761)
    sketchRapidDimensionBuilder12.SecondAssociativity.SetValue(edge21, workPart.ModelingViews.WorkView, point34)
    
    point1_35 = NXOpen.Point3d(-14.999999999999854, -3.5, 1.0614544448191761)
    point2_35 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder12.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge21, workPart.ModelingViews.WorkView, point1_35, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_35)
    
    point1_36 = NXOpen.Point3d(-12.303402589591892, -4.0, 0.91176228815702398)
    point2_36 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder12.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_36, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_36)
    
    point1_37 = NXOpen.Point3d(-14.999999999999854, -3.5, 1.0614544448191761)
    point2_37 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder12.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge21, workPart.ModelingViews.WorkView, point1_37, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_37)
    
    point1_38 = NXOpen.Point3d(-12.303402589591892, -4.0, 0.91176228815702398)
    point2_38 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder12.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_38, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_38)
    
    dimensionlinearunits313 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits314 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits315 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits316 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits317 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits318 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits319 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits320 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits321 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits322 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits323 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits324 = sketchRapidDimensionBuilder12.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin10 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin10.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin10.View = NXOpen.View.Null
    assocOrigin10.ViewOfGeometry = workPart.ModelingViews.WorkView
    point35 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin10.PointOnGeometry = point35
    assocOrigin10.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin10.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin10.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin10.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin10.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin10.DimensionLine = 0
    assocOrigin10.AssociatedView = NXOpen.View.Null
    assocOrigin10.AssociatedPoint = NXOpen.Point.Null
    assocOrigin10.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin10.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin10.XOffsetFactor = 0.0
    assocOrigin10.YOffsetFactor = 0.0
    assocOrigin10.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder12.Origin.SetAssociativeOrigin(assocOrigin10)
    
    point36 = NXOpen.Point3d(-14.331376193881589, -4.0, 5.5211635723291996)
    sketchRapidDimensionBuilder12.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point36)
    
    sketchRapidDimensionBuilder12.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder12.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder12.Style.DimensionStyle.TextCentered = False
    
    markId116 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject14 = sketchRapidDimensionBuilder12.Commit()
    
    theSession.DeleteUndoMark(markId116, None)
    
    theSession.SetUndoMarkName(markId115, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId115, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder12.Destroy()
    
    markId117 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder13 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines57 = []
    sketchRapidDimensionBuilder13.AppendedText.SetBefore(lines57)
    
    lines58 = []
    sketchRapidDimensionBuilder13.AppendedText.SetAfter(lines58)
    
    lines59 = []
    sketchRapidDimensionBuilder13.AppendedText.SetAbove(lines59)
    
    lines60 = []
    sketchRapidDimensionBuilder13.AppendedText.SetBelow(lines60)
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder13.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder13.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder13.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder13.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId117, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder13.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits325 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits326 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits327 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits328 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits329 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits330 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits331 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits332 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits333 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits334 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder13.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder13.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder13.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits335 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits336 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits337 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits338 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits339 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits340 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits341 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits342 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits343 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits344 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    expression73 = workPart.Expressions.FindObject("p21")
    expression73.SetFormula("3")
    
    theSession.SetUndoMarkVisibility(markId117, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId118 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId118, None)
    
    markId119 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId117, "Edit Driving Value")
    
    point1_39 = NXOpen.Point3d(-4.4399519722235326, -4.0, 0.52369097770650885)
    point2_39 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc3, workPart.ModelingViews.WorkView, point1_39, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_39)
    
    point1_40 = NXOpen.Point3d(-4.4399519722235326, -4.0, 0.52369097770650885)
    point2_40 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc3, workPart.ModelingViews.WorkView, point1_40, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_40)
    
    point1_41 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_41 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_41, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_41)
    
    dimensionlinearunits345 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits346 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits347 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits348 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits349 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits350 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    datumAxis3 = workPart.Datums.FindObject("DATUM_CSYS(0) Z axis")
    point37 = NXOpen.Point3d(0.0, 0.0, 1.0290201966191082)
    sketchRapidDimensionBuilder13.SecondAssociativity.SetValue(datumAxis3, workPart.ModelingViews.WorkView, point37)
    
    point1_42 = NXOpen.Point3d(0.0, 0.0, 1.0290201966191082)
    point2_42 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, datumAxis3, workPart.ModelingViews.WorkView, point1_42, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_42)
    
    point1_43 = NXOpen.Point3d(-4.4399519722235326, -4.0, 0.52369097770650885)
    point2_43 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc3, workPart.ModelingViews.WorkView, point1_43, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_43)
    
    point1_44 = NXOpen.Point3d(0.0, 0.0, 1.0290201966191082)
    point2_44 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, datumAxis3, workPart.ModelingViews.WorkView, point1_44, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_44)
    
    point1_45 = NXOpen.Point3d(-4.4399519722235326, -4.0, 0.52369097770650885)
    point2_45 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder13.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc3, workPart.ModelingViews.WorkView, point1_45, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_45)
    
    dimensionlinearunits351 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits352 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits353 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits354 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits355 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits356 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits357 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits358 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits359 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits360 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits361 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits362 = sketchRapidDimensionBuilder13.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin11 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin11.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin11.View = NXOpen.View.Null
    assocOrigin11.ViewOfGeometry = workPart.ModelingViews.WorkView
    point38 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin11.PointOnGeometry = point38
    assocOrigin11.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin11.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin11.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin11.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin11.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin11.DimensionLine = 0
    assocOrigin11.AssociatedView = NXOpen.View.Null
    assocOrigin11.AssociatedPoint = NXOpen.Point.Null
    assocOrigin11.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin11.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin11.XOffsetFactor = 0.0
    assocOrigin11.YOffsetFactor = 0.0
    assocOrigin11.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder13.Origin.SetAssociativeOrigin(assocOrigin11)
    
    point39 = NXOpen.Point3d(-1.5036310307527723, -4.0, 4.9373471047278876)
    sketchRapidDimensionBuilder13.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point39)
    
    sketchRapidDimensionBuilder13.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder13.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder13.Style.DimensionStyle.TextCentered = False
    
    markId120 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject15 = sketchRapidDimensionBuilder13.Commit()
    
    theSession.DeleteUndoMark(markId120, None)
    
    theSession.SetUndoMarkName(markId119, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId119, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder13.Destroy()
    
    markId121 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder14 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines61 = []
    sketchRapidDimensionBuilder14.AppendedText.SetBefore(lines61)
    
    lines62 = []
    sketchRapidDimensionBuilder14.AppendedText.SetAfter(lines62)
    
    lines63 = []
    sketchRapidDimensionBuilder14.AppendedText.SetAbove(lines63)
    
    lines64 = []
    sketchRapidDimensionBuilder14.AppendedText.SetBelow(lines64)
    
    sketchRapidDimensionBuilder14.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder14.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder14.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder14.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder14.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId121, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder14.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder14.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits363 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits364 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits365 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits366 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits367 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits368 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits369 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits370 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits371 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits372 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder14.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder14.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder14.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder14.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder14.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits373 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits374 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits375 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits376 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits377 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits378 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits379 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits380 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits381 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits382 = sketchRapidDimensionBuilder14.Style.UnitsStyle.DimensionLinearUnits
    
    expression74 = workPart.Expressions.FindObject("p22")
    expression74.SetFormula("4")
    
    theSession.SetUndoMarkVisibility(markId121, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId122 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId122, None)
    
    markId123 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId121, "Edit Driving Value")
    
    rotMatrix18 = NXOpen.Matrix3x3()
    
    rotMatrix18.Xx = 0.99733179925939019
    rotMatrix18.Xy = -0.034735663745878734
    rotMatrix18.Xz = 0.064208378348644235
    rotMatrix18.Yx = -0.062333345018096745
    rotMatrix18.Yy = 0.052608793916497559
    rotMatrix18.Yz = 0.99666788294873154
    rotMatrix18.Zx = -0.037997845792680521
    rotMatrix18.Zy = -0.99801089596596426
    rotMatrix18.Zz = 0.050303232980902411
    translation18 = NXOpen.Point3d(4.0467262996364912, -3.240427467455218, -4.3286894382196506)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix18, translation18, 16.315058804584158)
    
    rotMatrix19 = NXOpen.Matrix3x3()
    
    rotMatrix19.Xx = 0.98454276125452045
    rotMatrix19.Xy = -0.17474048651940385
    rotMatrix19.Xz = 0.011887541053048952
    rotMatrix19.Yx = -0.070540981536730676
    rotMatrix19.Yy = -0.33349470140405502
    rotMatrix19.Yz = 0.94010917135152727
    rotMatrix19.Zx = -0.16031070202940473
    rotMatrix19.Zy = -0.92641623825707198
    rotMatrix19.Zz = -0.34066615961738406
    translation19 = NXOpen.Point3d(4.1679021165698362, -3.0933053676639042, -3.5000066923999831)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix19, translation19, 16.315058804584158)
    
    scaleAboutPoint131 = NXOpen.Point3d(1.7838836510041938, -1.4919754172033362, 0.0)
    viewCenter131 = NXOpen.Point3d(-1.7838836510038176, 1.4919754172033652, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint131, viewCenter131)
    
    scaleAboutPoint132 = NXOpen.Point3d(1.5000839792535576, -1.4798125741283092, 0.0)
    viewCenter132 = NXOpen.Point3d(-1.5000839792531775, 1.479812574128337, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint132, viewCenter132)
    
    scaleAboutPoint133 = NXOpen.Point3d(2.432568615005652, -1.8497657176603906, 0.0)
    viewCenter133 = NXOpen.Point3d(-2.4325686150052763, 1.8497657176604188, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint133, viewCenter133)
    
    scaleAboutPoint134 = NXOpen.Point3d(1.9460548920045617, -1.4798125741283092, 0.0)
    viewCenter134 = NXOpen.Point3d(-1.9460548920041849, 1.479812574128337, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint134, viewCenter134)
    
    scaleAboutPoint135 = NXOpen.Point3d(1.5568439136036822, -1.1838500593026444, 0.0)
    viewCenter135 = NXOpen.Point3d(-1.556843913603309, 1.1838500593026722, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint135, viewCenter135)
    
    scaleAboutPoint136 = NXOpen.Point3d(1.2454751308829859, -0.94708004744211238, 0.0)
    viewCenter136 = NXOpen.Point3d(-1.2454751308826097, 0.94708004744214114, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint136, viewCenter136)
    
    scaleAboutPoint137 = NXOpen.Point3d(0.99638010470642591, -0.75766403795368731, 0.0)
    viewCenter137 = NXOpen.Point3d(-0.99638010470604887, 0.75766403795371562, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint137, viewCenter137)
    
    scaleAboutPoint138 = NXOpen.Point3d(0.79710408376517805, -0.60613123036294758, 0.0)
    viewCenter138 = NXOpen.Point3d(-0.7971040837648028, 0.60613123036297512, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint138, viewCenter138)
    
    scaleAboutPoint139 = NXOpen.Point3d(-0.24577375916068253, -0.32548416753735715, 0.0)
    viewCenter139 = NXOpen.Point3d(0.24577375916106142, 0.32548416753738491, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint139, viewCenter139)
    
    scaleAboutPoint140 = NXOpen.Point3d(-0.32382353402933844, -0.39024887434326305, 0.0)
    viewCenter140 = NXOpen.Point3d(0.32382353402971581, 0.39024887434329064, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint140, viewCenter140)
    
    scaleAboutPoint141 = NXOpen.Point3d(-0.40477941753672003, -0.47743213350505787, 0.0)
    viewCenter141 = NXOpen.Point3d(0.40477941753709878, 0.47743213350508618, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint141, viewCenter141)
    
    scaleAboutPoint142 = NXOpen.Point3d(-0.50597427192094646, -0.59679016688132669, 0.0)
    viewCenter142 = NXOpen.Point3d(0.50597427192132693, 0.59679016688135322, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint142, viewCenter142)
    
    rotMatrix20 = NXOpen.Matrix3x3()
    
    rotMatrix20.Xx = 0.98454276125452045
    rotMatrix20.Xy = -0.17474048651940385
    rotMatrix20.Xz = 0.011887541053048952
    rotMatrix20.Yx = -0.017952228025203316
    rotMatrix20.Yy = -0.033167197347258912
    rotMatrix20.Yz = 0.99928857420119643
    rotMatrix20.Zx = -0.17422189520911849
    rotMatrix20.Zy = -0.98405573998178175
    rotMatrix20.Zz = -0.035791505118574957
    translation20 = NXOpen.Point3d(2.8239209304785948, -2.9311219332904659, -4.4196310783244472)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix20, translation20, 16.315058804584162)
    
    perpendicularDimension2 = theSession.ActiveSketch.FindObject("ENTITY 26 5 1")
    point40 = NXOpen.Point3d(-3.8816054032128835, -4.0000000000000089, 0.52369097770650974)
    sketchRapidDimensionBuilder14.FirstAssociativity.SetValue(perpendicularDimension2, workPart.ModelingViews.WorkView, point40)
    
    line12 = theSession.ActiveSketch.FindObject("Curve DATUM17")
    point1_46 = NXOpen.Point3d(1.091132448697719, -4.0, 3.8476323829746399)
    point2_46 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder14.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line12, NXOpen.View.Null, point1_46, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_46)
    
    point1_47 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_47 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder14.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_47, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_47)
    
    sketchRapidDimensionBuilder14.Destroy()
    
    theSession.UndoToMark(markId123, None)
    
    theSession.DeleteUndoMark(markId123, None)
    
    sketchRapidDimensionBuilder14.Destroy()
    
    scaleAboutPoint143 = NXOpen.Point3d(0.12973699280047901, -2.2703973740050856, 0.0)
    viewCenter143 = NXOpen.Point3d(-0.12973699280010154, 2.2703973740051118, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint143, viewCenter143)
    
    scaleAboutPoint144 = NXOpen.Point3d(0.10378959424042082, -1.8163178992040663, 0.0)
    viewCenter144 = NXOpen.Point3d(-0.10378959424004361, 1.8163178992040927, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint144, viewCenter144)
    
    scaleAboutPoint145 = NXOpen.Point3d(0.083031675392373827, -1.4530543193632504, 0.0)
    viewCenter145 = NXOpen.Point3d(-0.083031675391997711, 1.4530543193632768, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint145, viewCenter145)
    
    scaleAboutPoint146 = NXOpen.Point3d(0.066425340313936571, -1.1624434554905971, 0.0)
    viewCenter146 = NXOpen.Point3d(-0.066425340313559927, 1.162443455490624, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint146, viewCenter146)
    
    scaleAboutPoint147 = NXOpen.Point3d(-0.039855204188062036, -0.94988236648659996, 0.0)
    viewCenter147 = NXOpen.Point3d(0.039855204188436973, 0.94988236648662605, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint147, viewCenter147)
    
    markId124 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Object Origin")
    
    horizontalDimension1.LeaderOrientation = NXOpen.Annotations.LeaderOrientation.FromLeft
    
    horizontalDimension1.IsOriginCentered = False
    
    origin17 = NXOpen.Point3d(-3.9912468949726092, -4.0, 0.19748566470605436)
    horizontalDimension1.AnnotationOrigin = origin17
    
    nErrs14 = theSession.UpdateManager.DoUpdate(markId124)
    
    markId125 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Object Origin")
    
    perpendicularDimension3 = nXObject15
    origin18 = NXOpen.Point3d(-1.7813931004303338, -4.0, 4.0310612096071186)
    perpendicularDimension3.AnnotationOrigin = origin18
    
    perpendicularDimension3.IsOriginCentered = False
    
    horizontalDimension1.LeaderOrientation = NXOpen.Annotations.LeaderOrientation.FromLeft
    
    horizontalDimension1.IsOriginCentered = False
    
    origin19 = NXOpen.Point3d(-4.7089609368737033, -4.0, -0.70880023041471529)
    horizontalDimension1.AnnotationOrigin = origin19
    
    nErrs15 = theSession.UpdateManager.DoUpdate(markId125)
    
    scaleAboutPoint148 = NXOpen.Point3d(-0.94589684606760061, -0.78116200208967745, 0.0)
    viewCenter148 = NXOpen.Point3d(0.94589684606797675, 0.78116200208970288, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint148, viewCenter148)
    
    scaleAboutPoint149 = NXOpen.Point3d(-0.75671747685404278, -0.62067837989165897, 0.0)
    viewCenter149 = NXOpen.Point3d(0.75671747685441837, 0.62067837989168473, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint149, viewCenter149)
    
    scaleAboutPoint150 = NXOpen.Point3d(-0.60537398148319621, -0.49654270391332456, 0.0)
    viewCenter150 = NXOpen.Point3d(0.60537398148357235, 0.4965427039133507, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint150, viewCenter150)
    
    scaleAboutPoint151 = NXOpen.Point3d(-0.48429918518651927, -0.39723416313065696, 0.0)
    viewCenter151 = NXOpen.Point3d(0.48429918518689558, 0.39723416313068316, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint151, viewCenter151)
    
    scaleAboutPoint152 = NXOpen.Point3d(-0.38743934814917852, -0.31778733050452335, 0.0)
    viewCenter152 = NXOpen.Point3d(0.38743934814955361, 0.31778733050454916, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint152, viewCenter152)
    
    scaleAboutPoint153 = NXOpen.Point3d(-0.29776237543145972, -0.24204076131577065, 0.0)
    viewCenter153 = NXOpen.Point3d(0.2977623754318352, 0.24204076131579649, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint153, viewCenter153)
    
    scaleAboutPoint154 = NXOpen.Point3d(-0.23681685999223345, -0.19223956869971737, 0.0)
    viewCenter154 = NXOpen.Point3d(0.23681685999260949, 0.19223956869974312, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint154, viewCenter154)
    
    scaleAboutPoint155 = NXOpen.Point3d(-0.29602107499033831, -0.24029946087464998, 0.0)
    viewCenter155 = NXOpen.Point3d(0.29602107499071539, 0.24029946087467596, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint155, viewCenter155)
    
    scaleAboutPoint156 = NXOpen.Point3d(-0.37002634373797022, -0.30037432609331549, 0.0)
    viewCenter156 = NXOpen.Point3d(0.37002634373834681, 0.30037432609334164, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint156, viewCenter156)
    
    scaleAboutPoint157 = NXOpen.Point3d(-0.46253292967251003, -0.37546790761664778, 0.0)
    viewCenter157 = NXOpen.Point3d(0.46253292967288634, 0.37546790761667398, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint157, viewCenter157)
    
    scaleAboutPoint158 = NXOpen.Point3d(-0.57816616209068483, -0.46933488452081285, 0.0)
    viewCenter158 = NXOpen.Point3d(0.5781661620910612, 0.46933488452083866, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint158, viewCenter158)
    
    scaleAboutPoint159 = NXOpen.Point3d(-0.72270770261340245, -0.58666860565101975, 0.0)
    viewCenter159 = NXOpen.Point3d(0.7227077026137787, 0.5866686056510455, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint159, viewCenter159)
    
    scaleAboutPoint160 = NXOpen.Point3d(-0.90338462826680044, -0.73333575706377818, 0.0)
    viewCenter160 = NXOpen.Point3d(0.90338462826717658, 0.73333575706380316, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint160, viewCenter160)
    
    scaleAboutPoint161 = NXOpen.Point3d(-1.1292307853335481, -0.64432580104335369, 0.0)
    viewCenter161 = NXOpen.Point3d(1.129230785333923, 0.64432580104337867, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint161, viewCenter161)
    
    scaleAboutPoint162 = NXOpen.Point3d(-1.4198416492061996, -0.8054072513041951, 0.0)
    viewCenter162 = NXOpen.Point3d(1.4198416492065746, 0.80540725130421986, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint162, viewCenter162)
    
    scaleAboutPoint163 = NXOpen.Point3d(-1.7748020615077977, -1.0067590641302473, 0.0)
    viewCenter163 = NXOpen.Point3d(1.7748020615081712, 1.0067590641302711, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint163, viewCenter163)
    
    scaleAboutPoint164 = NXOpen.Point3d(-2.2185025768847915, -1.2584488301628134, 0.0)
    viewCenter164 = NXOpen.Point3d(2.2185025768851663, 1.2584488301628356, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint164, viewCenter164)
    
    scaleAboutPoint165 = NXOpen.Point3d(-2.7731282211060373, -1.5730610377035192, 0.0)
    viewCenter165 = NXOpen.Point3d(2.7731282211064134, 1.5730610377035414, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint165, viewCenter165)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch Constraint->Dimension->Rapid...
    # ----------------------------------------------
    markId126 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder15 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines65 = []
    sketchRapidDimensionBuilder15.AppendedText.SetBefore(lines65)
    
    lines66 = []
    sketchRapidDimensionBuilder15.AppendedText.SetAfter(lines66)
    
    lines67 = []
    sketchRapidDimensionBuilder15.AppendedText.SetAbove(lines67)
    
    lines68 = []
    sketchRapidDimensionBuilder15.AppendedText.SetBelow(lines68)
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder15.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder15.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines69 = []
    sketchRapidDimensionBuilder15.AppendedText.SetBefore(lines69)
    
    lines70 = []
    sketchRapidDimensionBuilder15.AppendedText.SetAfter(lines70)
    
    lines71 = []
    sketchRapidDimensionBuilder15.AppendedText.SetAbove(lines71)
    
    lines72 = []
    sketchRapidDimensionBuilder15.AppendedText.SetBelow(lines72)
    
    theSession.SetUndoMarkName(markId126, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder15.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits383 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits384 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits385 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits386 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits387 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits388 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits389 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits390 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits391 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits392 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder15.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder15.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder15.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits393 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits394 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits395 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits396 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits397 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits398 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits399 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits400 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits401 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits402 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    rotMatrix21 = NXOpen.Matrix3x3()
    
    rotMatrix21.Xx = 0.99641197285795324
    rotMatrix21.Xy = -0.078948646436685879
    rotMatrix21.Xz = 0.03050068148649485
    rotMatrix21.Yx = -0.016432463963353124
    rotMatrix21.Yy = 0.17305913884859328
    rotMatrix21.Yz = 0.9847743439941361
    rotMatrix21.Zx = -0.083025023176260107
    rotMatrix21.Zy = -0.98174214826847761
    rotMatrix21.Zz = 0.17114087717369908
    translation21 = NXOpen.Point3d(0.14052407160684016, -2.8052601138746822, -5.4141524379426897)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix21, translation21, 13.052047043667342)
    
    point1_48 = NXOpen.Point3d(-12.42202664181165, -4.0, 0.52369097770650885)
    point2_48 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder15.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_48, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_48)
    
    point1_49 = NXOpen.Point3d(-12.42202664181165, -4.0, 0.52369097770650885)
    point2_49 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder15.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_49, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_49)
    
    point1_50 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_50 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder15.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_50, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_50)
    
    dimensionlinearunits403 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits404 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits405 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits406 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits407 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits408 = sketchRapidDimensionBuilder15.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin12 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin12.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin12.View = NXOpen.View.Null
    assocOrigin12.ViewOfGeometry = workPart.ModelingViews.WorkView
    point41 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin12.PointOnGeometry = point41
    assocOrigin12.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin12.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin12.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin12.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin12.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin12.DimensionLine = 0
    assocOrigin12.AssociatedView = NXOpen.View.Null
    assocOrigin12.AssociatedPoint = NXOpen.Point.Null
    assocOrigin12.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin12.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin12.XOffsetFactor = 0.0
    assocOrigin12.YOffsetFactor = 0.0
    assocOrigin12.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder15.Origin.SetAssociativeOrigin(assocOrigin12)
    
    point42 = NXOpen.Point3d(-13.861416562381171, -4.0, 1.8793351935502403)
    sketchRapidDimensionBuilder15.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point42)
    
    sketchRapidDimensionBuilder15.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder15.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder15.Style.DimensionStyle.TextCentered = False
    
    markId127 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject16 = sketchRapidDimensionBuilder15.Commit()
    
    theSession.DeleteUndoMark(markId127, None)
    
    theSession.SetUndoMarkName(markId126, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId126, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder15.Destroy()
    
    markId128 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder16 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines73 = []
    sketchRapidDimensionBuilder16.AppendedText.SetBefore(lines73)
    
    lines74 = []
    sketchRapidDimensionBuilder16.AppendedText.SetAfter(lines74)
    
    lines75 = []
    sketchRapidDimensionBuilder16.AppendedText.SetAbove(lines75)
    
    lines76 = []
    sketchRapidDimensionBuilder16.AppendedText.SetBelow(lines76)
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder16.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder16.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder16.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder16.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId128, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder16.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits409 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits410 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits411 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits412 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits413 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits414 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits415 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits416 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits417 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits418 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder16.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder16.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder16.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder16.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits419 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits420 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits421 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits422 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits423 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits424 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits425 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits426 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits427 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits428 = sketchRapidDimensionBuilder16.Style.UnitsStyle.DimensionLinearUnits
    
    expression75 = workPart.Expressions.FindObject("p23")
    expression75.SetFormula("0.6")
    
    theSession.SetUndoMarkVisibility(markId128, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId129 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId129, None)
    
    markId130 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId128, "Edit Driving Value")
    
    rotMatrix22 = NXOpen.Matrix3x3()
    
    rotMatrix22.Xx = 0.99868527139100371
    rotMatrix22.Xy = -0.033571384155699185
    rotMatrix22.Xz = 0.038738751561602461
    rotMatrix22.Yx = -0.038704140221905659
    rotMatrix22.Yy = 0.0016804680428126467
    rotMatrix22.Yz = 0.99924930100393106
    rotMatrix22.Zx = -0.033611281385334563
    rotMatrix22.Zy = -0.99943490943284274
    rotMatrix22.Zz = 0.00037890712359530537
    translation22 = NXOpen.Point3d(0.10349734821800846, -2.8742382186610818, -4.6322438446930194)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix22, translation22, 13.052047043667342)
    
    sketchRapidDimensionBuilder16.Destroy()
    
    theSession.UndoToMark(markId130, None)
    
    theSession.DeleteUndoMark(markId130, None)
    
    sketchRapidDimensionBuilder16.Destroy()
    
    # ----------------------------------------------
    #   Menu: File->Finish Sketch
    # ----------------------------------------------
    sketch6 = theSession.ActiveSketch
    
    markId131 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId132 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder5 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section5 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder5.Section = section5
    
    extrudeBuilder5.AllowSelfIntersectingSection(True)
    
    expression76 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder5.DistanceTolerance = 0.01
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies18 = [NXOpen.Body.Null] * 1 
    targetBodies18[0] = NXOpen.Body.Null
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies18)
    
    extrudeBuilder5.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder5.Limits.EndExtend.Value.SetFormula("8")
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies19 = [NXOpen.Body.Null] * 1 
    targetBodies19[0] = NXOpen.Body.Null
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies19)
    
    extrudeBuilder5.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder5.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder5.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder5.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder5 = extrudeBuilder5.SmartVolumeProfile
    
    smartVolumeProfileBuilder5.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder5.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId132, "Extrude Dialog")
    
    section5.DistanceTolerance = 0.01
    
    section5.ChainingTolerance = 0.0094999999999999998
    
    section5.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId133 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId134 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    features3 = [NXOpen.Features.Feature.Null] * 1 
    sketchFeature3 = feature8
    features3[0] = sketchFeature3
    curveFeatureRule3 = workPart.ScRuleFactory.CreateRuleCurveFeature(features3)
    
    section5.AllowSelfIntersection(True)
    
    rules26 = [None] * 1 
    rules26[0] = curveFeatureRule3
    helpPoint3 = NXOpen.Point3d(-12.223069204220721, -4.0, 0.23494196086687616)
    section5.AddToSection(rules26, arc2, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint3, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId134, None)
    
    direction7 = workPart.Directions.CreateDirection(sketch6, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder5.Direction = direction7
    
    targetBodies20 = [NXOpen.Body.Null] * 1 
    targetBodies20[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies20)
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies21 = [NXOpen.Body.Null] * 1 
    targetBodies21[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies21)
    
    expression77 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId133, None)
    
    rotMatrix23 = NXOpen.Matrix3x3()
    
    rotMatrix23.Xx = 0.81430363997010458
    rotMatrix23.Xy = -0.5751775157126624
    rotMatrix23.Xz = 0.077976966791798483
    rotMatrix23.Yx = 0.10311442815723561
    rotMatrix23.Yy = 0.27555338500709253
    rotMatrix23.Yz = 0.95573937175201684
    rotMatrix23.Zx = -0.57120661466517153
    rotMatrix23.Zy = -0.77022149894023673
    rotMatrix23.Zz = 0.28369322503896932
    translation23 = NXOpen.Point3d(-11.435384000959029, -2.9079858733216581, -3.587094673004219)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix23, translation23, 6.6826480863576707)
    
    direction8 = extrudeBuilder5.Direction
    
    success2 = direction8.ReverseDirection()
    
    extrudeBuilder5.Direction = direction8
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies22 = [NXOpen.Body.Null] * 1 
    targetBodies22[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies22)
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies23 = [NXOpen.Body.Null] * 1 
    targetBodies23[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies23)
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies24 = [NXOpen.Body.Null] * 1 
    targetBodies24[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies24)
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies25 = [NXOpen.Body.Null] * 1 
    targetBodies25[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies25)
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies26 = [NXOpen.Body.Null] * 1 
    targetBodies26[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies26)
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies27 = [NXOpen.Body.Null] * 1 
    targetBodies27[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies27)
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies28 = [NXOpen.Body.Null] * 1 
    targetBodies28[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies28)
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies29 = [NXOpen.Body.Null] * 1 
    targetBodies29[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies29)
    
    extrudeBuilder5.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies30 = [NXOpen.Body.Null] * 1 
    targetBodies30[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies30)
    
    markId135 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder5.ParentFeatureInternal = False
    
    feature9 = extrudeBuilder5.CommitFeature()
    
    theSession.DeleteUndoMark(markId135, None)
    
    theSession.SetUndoMarkName(markId132, "Extrude")
    
    expression78 = extrudeBuilder5.Limits.StartExtend.Value
    expression79 = extrudeBuilder5.Limits.EndExtend.Value
    extrudeBuilder5.Destroy()
    
    workPart.Expressions.Delete(expression76)
    
    workPart.Expressions.Delete(expression77)
    
    markId136 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder6 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section6 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder6.Section = section6
    
    extrudeBuilder6.AllowSelfIntersectingSection(True)
    
    expression80 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder6.DistanceTolerance = 0.01
    
    extrudeBuilder6.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies31 = [NXOpen.Body.Null] * 1 
    targetBodies31[0] = NXOpen.Body.Null
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies31)
    
    extrudeBuilder6.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder6.Limits.EndExtend.Value.SetFormula("15")
    
    extrudeBuilder6.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies32 = [NXOpen.Body.Null] * 1 
    targetBodies32[0] = NXOpen.Body.Null
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies32)
    
    extrudeBuilder6.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder6.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder6.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder6.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder6 = extrudeBuilder6.SmartVolumeProfile
    
    smartVolumeProfileBuilder6.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder6.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId136, "Extrude Dialog")
    
    section6.DistanceTolerance = 0.01
    
    section6.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   Dialog Begin Extrude
    # ----------------------------------------------
    section6.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    rotMatrix24 = NXOpen.Matrix3x3()
    
    rotMatrix24.Xx = 0.9987534942968298
    rotMatrix24.Xy = 0.0018482085967863673
    rotMatrix24.Xz = -0.049880274205914281
    rotMatrix24.Yx = 0.04969985795120619
    rotMatrix24.Yy = 0.05575338497942426
    rotMatrix24.Yz = 0.99720684122350889
    rotMatrix24.Zx = 0.0046240403874044508
    rotMatrix24.Zy = -0.99844285975128477
    rotMatrix24.Zz = 0.055592032362351877
    translation24 = NXOpen.Point3d(-9.6544032007703251, -3.4375495333466057, 1.4409779860836049)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix24, translation24, 6.6826480863576707)
    
    point43 = workPart.Points.CreatePoint(edge19, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction9 = workPart.Directions.CreateDirection(edge20, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform4 = workPart.Xforms.CreateXformByPlaneXDirPoint(face3, direction9, point43, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem4 = workPart.CoordinateSystems.CreateCoordinateSystem(xform4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder1 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder1.Csys = cartesianCoordinateSystem4
    
    datumCsysBuilder1.DisplayScaleFactor = 1.25
    
    feature10 = datumCsysBuilder1.CommitFeature()
    
    datumCsysBuilder1.Destroy()
    
    markId137 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder4 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder4.Csystem = cartesianCoordinateSystem4
    
    sketchInPlaceBuilder4.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject17 = sketchInPlaceBuilder4.Commit()
    
    sketchInPlaceBuilder4.Destroy()
    
    sketch7 = nXObject17
    sketch7.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId138 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId138, None, True)
    
    markId139 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_003")
    
    markId140 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    scaleAboutPoint166 = NXOpen.Point3d(10.59101732607378, 2.2171849355518711, 0.0)
    viewCenter166 = NXOpen.Point3d(-10.591017326073414, -2.2171849355518436, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint166, viewCenter166)
    
    scaleAboutPoint167 = NXOpen.Point3d(13.238771657592173, 2.7219904342712651, 0.0)
    viewCenter167 = NXOpen.Point3d(-13.238771657591819, -2.7219904342712393, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint167, viewCenter167)
    
    scaleAboutPoint168 = NXOpen.Point3d(16.54846457199017, 3.4024880428390811, 0.0)
    viewCenter168 = NXOpen.Point3d(-16.548464571989818, -3.4024880428390487, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint168, viewCenter168)
    
    scaleAboutPoint169 = NXOpen.Point3d(20.685580714987662, 4.253110053548844, 0.0)
    viewCenter169 = NXOpen.Point3d(-20.685580714987296, -4.2531100535488164, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint169, viewCenter169)
    
    scaleAboutPoint170 = NXOpen.Point3d(16.610327990950871, 3.4024880428390811, 0.0)
    viewCenter170 = NXOpen.Point3d(-16.61032799095052, -3.4024880428390487, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint170, viewCenter170)
    
    scaleAboutPoint171 = NXOpen.Point3d(13.585206803772147, 2.7219904342712646, 0.0)
    viewCenter171 = NXOpen.Point3d(-13.585206803771797, -2.7219904342712389, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint171, viewCenter171)
    
    scaleAboutPoint172 = NXOpen.Point3d(11.066128383692012, 2.1775923474170149, 0.0)
    viewCenter172 = NXOpen.Point3d(-11.066128383691661, -2.1775923474169874, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint172, viewCenter172)
    
    scaleAboutPoint173 = NXOpen.Point3d(8.8845767774615325, 1.7420738779336145, 0.0)
    viewCenter173 = NXOpen.Point3d(-8.8845767774611843, -1.7420738779335869, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint173, viewCenter173)
    
    scaleAboutPoint174 = NXOpen.Point3d(7.107661421969266, 1.3936591023468938, 0.0)
    viewCenter174 = NXOpen.Point3d(-7.1076614219689107, -1.3936591023468652, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint174, viewCenter174)
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Circle...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId140, "Curve")
    
    markId141 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId142 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId142, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix4 = theSession.ActiveSketch.Orientation
    
    center7 = NXOpen.Point3d(-3.5152542316044526, -4.0, 0.634798617759053)
    arc4 = workPart.Curves.CreateArc(center7, nXMatrix4, 0.8074364481878501, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_15 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_15.Geometry = arc4
    dimObject1_15.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_15.AssocValue = 0
    dimObject1_15.HelpPoint.X = 0.0
    dimObject1_15.HelpPoint.Y = 0.0
    dimObject1_15.HelpPoint.Z = 0.0
    dimObject1_15.View = NXOpen.NXObject.Null
    dimOrigin15 = NXOpen.Point3d(-3.5152542316044526, -4.0, 0.86464762075169532)
    sketchDimensionalConstraint15 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_15, dimOrigin15, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension15 = sketchDimensionalConstraint15.AssociatedDimension
    
    expression81 = sketchDimensionalConstraint15.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Dimensions->Rapid...
    # ----------------------------------------------
    markId143 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchRapidDimensionBuilder17 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines77 = []
    sketchRapidDimensionBuilder17.AppendedText.SetBefore(lines77)
    
    lines78 = []
    sketchRapidDimensionBuilder17.AppendedText.SetAfter(lines78)
    
    lines79 = []
    sketchRapidDimensionBuilder17.AppendedText.SetAbove(lines79)
    
    lines80 = []
    sketchRapidDimensionBuilder17.AppendedText.SetBelow(lines80)
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder17.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder17.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines81 = []
    sketchRapidDimensionBuilder17.AppendedText.SetBefore(lines81)
    
    lines82 = []
    sketchRapidDimensionBuilder17.AppendedText.SetAfter(lines82)
    
    lines83 = []
    sketchRapidDimensionBuilder17.AppendedText.SetAbove(lines83)
    
    lines84 = []
    sketchRapidDimensionBuilder17.AppendedText.SetBelow(lines84)
    
    theSession.SetUndoMarkName(markId143, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder17.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits429 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits430 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits431 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits432 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits433 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits434 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits435 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits436 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits437 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits438 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder17.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder17.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder17.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits439 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits440 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits441 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits442 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits443 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits444 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits445 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits446 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits447 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits448 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    point1_51 = NXOpen.Point3d(-3.0516085714212409, -4.0, 1.295848025636773)
    point2_51 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder17.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc4, workPart.ModelingViews.WorkView, point1_51, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_51)
    
    point1_52 = NXOpen.Point3d(-3.0516085714212409, -4.0, 1.295848025636773)
    point2_52 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder17.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc4, workPart.ModelingViews.WorkView, point1_52, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_52)
    
    point1_53 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_53 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder17.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_53, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_53)
    
    dimensionlinearunits449 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits450 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits451 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits452 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits453 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits454 = sketchRapidDimensionBuilder17.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin13 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin13.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin13.View = NXOpen.View.Null
    assocOrigin13.ViewOfGeometry = workPart.ModelingViews.WorkView
    point44 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin13.PointOnGeometry = point44
    assocOrigin13.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin13.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin13.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin13.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin13.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin13.DimensionLine = 0
    assocOrigin13.AssociatedView = NXOpen.View.Null
    assocOrigin13.AssociatedPoint = NXOpen.Point.Null
    assocOrigin13.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin13.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin13.XOffsetFactor = 0.0
    assocOrigin13.YOffsetFactor = 0.0
    assocOrigin13.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder17.Origin.SetAssociativeOrigin(assocOrigin13)
    
    point45 = NXOpen.Point3d(-1.0778598587585004, -4.0, 3.9012197717704966)
    sketchRapidDimensionBuilder17.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point45)
    
    sketchRapidDimensionBuilder17.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder17.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder17.Style.DimensionStyle.TextCentered = False
    
    markId144 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject18 = sketchRapidDimensionBuilder17.Commit()
    
    theSession.DeleteUndoMark(markId144, None)
    
    theSession.SetUndoMarkName(markId143, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId143, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder17.Destroy()
    
    markId145 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder18 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines85 = []
    sketchRapidDimensionBuilder18.AppendedText.SetBefore(lines85)
    
    lines86 = []
    sketchRapidDimensionBuilder18.AppendedText.SetAfter(lines86)
    
    lines87 = []
    sketchRapidDimensionBuilder18.AppendedText.SetAbove(lines87)
    
    lines88 = []
    sketchRapidDimensionBuilder18.AppendedText.SetBelow(lines88)
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder18.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder18.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder18.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder18.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId145, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder18.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits455 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits456 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits457 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits458 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits459 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits460 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits461 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits462 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits463 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits464 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder18.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder18.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder18.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits465 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits466 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits467 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits468 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits469 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits470 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits471 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits472 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits473 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits474 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    # ----------------------------------------------
    #   Menu: View->Maximize Resource Bar Tab
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: View->Maximize Resource Bar Tab
    # ----------------------------------------------
    expression82 = workPart.Expressions.FindObject("p33")
    expression82.SetFormula("0.6")
    
    theSession.SetUndoMarkVisibility(markId145, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId146 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.Scale(0.37154626927295481)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId146, None)
    
    markId147 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId145, "Edit Driving Value")
    
    point1_54 = NXOpen.Point3d(-6.7838235909961542, -4.0, 0.61092469334280819)
    point2_54 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc4, workPart.ModelingViews.WorkView, point1_54, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_54)
    
    point1_55 = NXOpen.Point3d(-6.7838235909961542, -4.0, 0.61092469334280819)
    point2_55 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc4, workPart.ModelingViews.WorkView, point1_55, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_55)
    
    point1_56 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_56 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_56, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_56)
    
    dimensionlinearunits475 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits476 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits477 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits478 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits479 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits480 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    point1_57 = NXOpen.Point3d(-12.080114986078936, -4.0, 0.72777571660927265)
    point2_57 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_57, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_57)
    
    point1_58 = NXOpen.Point3d(-6.7838235909961542, -4.0, 0.61092469334280819)
    point2_58 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc4, workPart.ModelingViews.WorkView, point1_58, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_58)
    
    point1_59 = NXOpen.Point3d(-12.080114986078936, -4.0, 0.72777571660927265)
    point2_59 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_59, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_59)
    
    point1_60 = NXOpen.Point3d(-6.7838235909961542, -4.0, 0.61092469334280819)
    point2_60 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc4, workPart.ModelingViews.WorkView, point1_60, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_60)
    
    point1_61 = NXOpen.Point3d(-12.080114986078936, -4.0, 0.72777571660927265)
    point2_61 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder18.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc2, workPart.ModelingViews.WorkView, point1_61, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_61)
    
    dimensionlinearunits481 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits482 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits483 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits484 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits485 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits486 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits487 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits488 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits489 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits490 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits491 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits492 = sketchRapidDimensionBuilder18.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin14 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin14.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin14.View = NXOpen.View.Null
    assocOrigin14.ViewOfGeometry = workPart.ModelingViews.WorkView
    point46 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin14.PointOnGeometry = point46
    assocOrigin14.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin14.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin14.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin14.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin14.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin14.DimensionLine = 0
    assocOrigin14.AssociatedView = NXOpen.View.Null
    assocOrigin14.AssociatedPoint = NXOpen.Point.Null
    assocOrigin14.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin14.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin14.XOffsetFactor = 0.0
    assocOrigin14.YOffsetFactor = 0.0
    assocOrigin14.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder18.Origin.SetAssociativeOrigin(assocOrigin14)
    
    point47 = NXOpen.Point3d(-10.05809232915367, -4.0, 7.6514297199039216)
    sketchRapidDimensionBuilder18.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point47)
    
    sketchRapidDimensionBuilder18.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder18.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder18.Style.DimensionStyle.TextCentered = False
    
    markId148 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    nXObject19 = sketchRapidDimensionBuilder18.Commit()
    
    theSession.DeleteUndoMark(markId148, None)
    
    theSession.SetUndoMarkName(markId147, "Rapid Dimension")
    
    theSession.SetUndoMarkVisibility(markId147, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder18.Destroy()
    
    markId149 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder19 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines89 = []
    sketchRapidDimensionBuilder19.AppendedText.SetBefore(lines89)
    
    lines90 = []
    sketchRapidDimensionBuilder19.AppendedText.SetAfter(lines90)
    
    lines91 = []
    sketchRapidDimensionBuilder19.AppendedText.SetAbove(lines91)
    
    lines92 = []
    sketchRapidDimensionBuilder19.AppendedText.SetBelow(lines92)
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder19.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder19.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder19.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder19.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId149, "Rapid Dimension Dialog")
    
    sketchRapidDimensionBuilder19.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits493 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits494 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits495 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits496 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits497 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits498 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits499 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits500 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits501 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits502 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder19.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder19.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder19.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder19.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits503 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits504 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits505 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits506 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits507 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits508 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits509 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits510 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits511 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits512 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    expression83 = workPart.Expressions.FindObject("p34")
    expression83.SetFormula("8")
    
    theSession.SetUndoMarkVisibility(markId149, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId150 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId150, None)
    
    markId151 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Rapid Dimension")
    
    theSession.SetUndoMarkName(markId149, "Edit Driving Value")
    
    point1_62 = NXOpen.Point3d(-4.0001861275184032, -4.0, 0.43569642700548805)
    point2_62 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc4, workPart.ModelingViews.WorkView, point1_62, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_62)
    
    point1_63 = NXOpen.Point3d(-4.0001861275184032, -4.0, 0.43569642700548805)
    point2_63 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc4, workPart.ModelingViews.WorkView, point1_63, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_63)
    
    point1_64 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_64 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_64, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_64)
    
    dimensionlinearunits513 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits514 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits515 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits516 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits517 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits518 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    point48 = NXOpen.Point3d(-3.5306998788890103, -4.0, -2.0376368494323395e-16)
    sketchRapidDimensionBuilder19.SecondAssociativity.SetValue(edge20, workPart.ModelingViews.WorkView, point48)
    
    point1_65 = NXOpen.Point3d(-3.5306998788890103, -4.0, -2.0376368494323395e-16)
    point2_65 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge20, workPart.ModelingViews.WorkView, point1_65, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_65)
    
    point1_66 = NXOpen.Point3d(-4.0001861275184032, -4.0, 0.43569642700548805)
    point2_66 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc4, workPart.ModelingViews.WorkView, point1_66, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_66)
    
    point1_67 = NXOpen.Point3d(-3.5306998788890103, -4.0, -2.0376368494323395e-16)
    point2_67 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge20, workPart.ModelingViews.WorkView, point1_67, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_67)
    
    point1_68 = NXOpen.Point3d(-4.0001861275184032, -4.0, 0.43569642700548805)
    point2_68 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder19.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc4, workPart.ModelingViews.WorkView, point1_68, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_68)
    
    dimensionlinearunits519 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits520 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits521 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits522 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits523 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits524 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits525 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits526 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits527 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits528 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits529 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits530 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits531 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits532 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits533 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits534 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits535 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits536 = sketchRapidDimensionBuilder19.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder19.Destroy()
    
    theSession.UndoToMark(markId151, None)
    
    theSession.DeleteUndoMark(markId151, None)
    
    sketchRapidDimensionBuilder19.Destroy()
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Line...
    # ----------------------------------------------
    markId152 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId153 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId153, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    startPoint15 = NXOpen.Point3d(-12.299999999999828, -4.0, 0.52369097770650885)
    endPoint15 = NXOpen.Point3d(-3.0999999999998273, -4.0, 0.52369097770650885)
    line13 = workPart.Curves.CreateLine(startPoint15, endPoint15)
    
    theSession.ActiveSketch.AddGeometry(line13, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_16 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_16.Geometry = line13
    geom1_16.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_16.SplineDefiningPointIndex = 0
    geom2_16 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_16.Geometry = arc2
    geom2_16.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom2_16.SplineDefiningPointIndex = 0
    sketchGeometricConstraint21 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_16, geom2_16)
    
    geom13 = NXOpen.Sketch.ConstraintGeometry()
    
    geom13.Geometry = line13
    geom13.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom13.SplineDefiningPointIndex = 0
    sketchGeometricConstraint22 = theSession.ActiveSketch.CreateHorizontalConstraint(geom13)
    
    dimObject1_16 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_16.Geometry = line13
    dimObject1_16.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_16.AssocValue = 0
    dimObject1_16.HelpPoint.X = 0.0
    dimObject1_16.HelpPoint.Y = 0.0
    dimObject1_16.HelpPoint.Z = 0.0
    dimObject1_16.View = NXOpen.NXObject.Null
    dimObject2_12 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_12.Geometry = line13
    dimObject2_12.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_12.AssocValue = 0
    dimObject2_12.HelpPoint.X = 0.0
    dimObject2_12.HelpPoint.Y = 0.0
    dimObject2_12.HelpPoint.Z = 0.0
    dimObject2_12.View = NXOpen.NXObject.Null
    dimOrigin16 = NXOpen.Point3d(-7.6999999999998279, -4.0, -0.16585603127141813)
    sketchDimensionalConstraint16 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_16, dimObject2_12, dimOrigin16, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint9 = sketchDimensionalConstraint16
    dimension16 = sketchHelpedDimensionalConstraint9.AssociatedDimension
    
    expression84 = sketchHelpedDimensionalConstraint9.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    # ----------------------------------------------
    #   Dialog Begin Line
    # ----------------------------------------------
    scaleAboutPoint175 = NXOpen.Point3d(0.1114927281879278, -0.93248463575207885, 0.0)
    viewCenter175 = NXOpen.Point3d(-0.11149272818757247, 0.93248463575210883, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint175, viewCenter175)
    
    scaleAboutPoint176 = NXOpen.Point3d(0.089194182550374784, -0.74598770860166175, 0.0)
    viewCenter176 = NXOpen.Point3d(-0.089194182550024037, 0.74598770860169006, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint176, viewCenter176)
    
    markId154 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId155 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    conGeom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_3.Geometry = arc4
    conGeom1_3.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    conGeom1_3.SplineDefiningPointIndex = 0
    conGeom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_3.Geometry = line13
    conGeom2_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_3.SplineDefiningPointIndex = 0
    help3 = NXOpen.Sketch.ConstraintGeometryHelp()
    
    help3.Type = NXOpen.Sketch.ConstraintGeometryHelpType.Point
    help3.Point.X = -4.2110082348855418
    help3.Point.Y = -4.0
    help3.Point.Z = 0.52369097770650885
    help3.Parameter = 0.0
    sketchHelpedGeometricConstraint3 = theSession.ActiveSketch.CreatePointOnCurveConstraint(conGeom1_3, conGeom2_3, help3)
    
    theSession.SetUndoMarkVisibility(markId155, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    perpendicularDimension4 = theSession.ActiveSketch.FindObject("ENTITY 26 4 1")
    theSession.UpdateManager.LogForUpdate(perpendicularDimension4)
    
    center8 = NXOpen.Point3d(-4.2999999999998275, -4.0, 0.52369097770650885)
    arc4.SetParameters(0.29999999999999982, center8, 0.0, ( 360.0 * math.pi/180.0 ))
    
    sketchHelpedDimensionalConstraint10 = theSession.ActiveSketch.FindObject("ENTITY 243 12 1")
    sketchHelpedDimensionalConstraint10.Refresh()
    
    sketchHelpedDimensionalConstraint11 = theSession.ActiveSketch.FindObject("DimensionalConstraint p34")
    helpPoint1_4 = NXOpen.Point3d(-3.9999999999998277, -4.0, 0.52369097770650896)
    helpPoint2_4 = NXOpen.Point3d(-11.999999999999828, -4.0, 0.52369097770650896)
    sketchHelpedDimensionalConstraint11.SetHelpPoints(True, True, helpPoint1_4, helpPoint2_4)
    
    nErrs16 = theSession.UpdateManager.DoUpdate(markId155)
    
    geoms10 = [NXOpen.SmartObject.Null] * 1 
    geoms10[0] = arc4
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms10)
    
    geoms11 = [NXOpen.SmartObject.Null] * 1 
    geoms11[0] = arc4
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms11)
    
    geoms12 = [NXOpen.SmartObject.Null] * 1 
    geoms12[0] = arc4
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms12)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId156 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    markId157 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Delete")
    
    objects7 = [NXOpen.NXObject.Null] * 1 
    objects7[0] = line13
    errorList1 = theSession.ActiveSketch.DeleteObjects(objects7)
    
    errorList1.Dispose()
    theSession.DeleteUndoMark(markId156, None)
    
    scaleAboutPoint177 = NXOpen.Point3d(1.2908830783630751, 4.592689545130332, 0.0)
    viewCenter177 = NXOpen.Point3d(-1.2908830783627245, -4.5926895451303036, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint177, viewCenter177)
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    theSession.Preferences.Sketch.SectionView = False
    
    markId158 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId137, None)
    
    section6.DistanceTolerance = 0.01
    
    section6.ChainingTolerance = 0.0094999999999999998
    
    markId159 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves1 = [NXOpen.ICurve.Null] * 1 
    curves1[0] = arc4
    seedPoint1 = NXOpen.Point3d(-4.1999999999998261, -4.0, 0.52369097770650885)
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch7, curves1, seedPoint1, 0.01)
    
    section6.AllowSelfIntersection(True)
    
    rules27 = [None] * 1 
    rules27[0] = regionBoundaryRule1
    helpPoint4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section6.AddToSection(rules27, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint4, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId159, None)
    
    expression85 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    refs1 = section6.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression85)
    
    expression86 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    direction10 = workPart.Directions.CreateDirection(sketch7, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder6.Direction = direction10
    
    targetBodies33 = [NXOpen.Body.Null] * 1 
    targetBodies33[0] = body1
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies33)
    
    extrudeBuilder6.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies34 = [NXOpen.Body.Null] * 1 
    targetBodies34[0] = body1
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies34)
    
    rotMatrix25 = NXOpen.Matrix3x3()
    
    rotMatrix25.Xx = 0.90631219086897685
    rotMatrix25.Xy = -0.42226586598046573
    rotMatrix25.Xz = -0.017022077136607444
    rotMatrix25.Yx = 0.069676224959295305
    rotMatrix25.Yy = 0.1095765968668925
    rotMatrix25.Yz = 0.99153325365037304
    rotMatrix25.Zx = -0.41682542671686779
    rotMatrix25.Zy = -0.89982470951115945
    rotMatrix25.Zz = 0.12873249704508644
    translation25 = NXOpen.Point3d(-10.449894484040005, -3.2700832159160105, -1.9473432004575519)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix25, translation25, 6.5337666840518027)
    
    direction11 = extrudeBuilder6.Direction
    
    success3 = direction11.ReverseDirection()
    
    extrudeBuilder6.Direction = direction11
    
    extrudeBuilder6.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies35 = [NXOpen.Body.Null] * 1 
    targetBodies35[0] = body1
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies35)
    
    extrudeBuilder6.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies36 = [NXOpen.Body.Null] * 1 
    targetBodies36[0] = body1
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies36)
    
    extrudeBuilder6.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies37 = [NXOpen.Body.Null] * 1 
    targetBodies37[0] = body1
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies37)
    
    extrudeBuilder6.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies38 = [NXOpen.Body.Null] * 1 
    targetBodies38[0] = body1
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies38)
    
    extrudeBuilder6.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies39 = [NXOpen.Body.Null] * 1 
    targetBodies39[0] = body1
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies39)
    
    extrudeBuilder6.Limits.EndExtend.Value.SetFormula("28")
    
    extrudeBuilder6.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies40 = [NXOpen.Body.Null] * 1 
    targetBodies40[0] = body1
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies40)
    
    markId160 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder6.ParentFeatureInternal = True
    
    feature11 = extrudeBuilder6.CommitFeature()
    
    theSession.DeleteUndoMark(markId160, None)
    
    theSession.SetUndoMarkName(markId136, "Extrude")
    
    expression87 = extrudeBuilder6.Limits.StartExtend.Value
    expression88 = extrudeBuilder6.Limits.EndExtend.Value
    extrudeBuilder6.Destroy()
    
    workPart.Expressions.Delete(expression80)
    
    workPart.Expressions.Delete(expression86)
    
    markId161 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder7 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section7 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder7.Section = section7
    
    extrudeBuilder7.AllowSelfIntersectingSection(True)
    
    expression89 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder7.DistanceTolerance = 0.01
    
    extrudeBuilder7.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies41 = [NXOpen.Body.Null] * 1 
    targetBodies41[0] = NXOpen.Body.Null
    extrudeBuilder7.BooleanOperation.SetTargetBodies(targetBodies41)
    
    extrudeBuilder7.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder7.Limits.EndExtend.Value.SetFormula("28")
    
    extrudeBuilder7.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies42 = [NXOpen.Body.Null] * 1 
    targetBodies42[0] = NXOpen.Body.Null
    extrudeBuilder7.BooleanOperation.SetTargetBodies(targetBodies42)
    
    extrudeBuilder7.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder7.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder7.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder7.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder7 = extrudeBuilder7.SmartVolumeProfile
    
    smartVolumeProfileBuilder7.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder7.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId161, "Extrude Dialog")
    
    section7.DistanceTolerance = 0.01
    
    section7.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   Dialog Begin Extrude
    # ----------------------------------------------
    section7.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    rotMatrix26 = NXOpen.Matrix3x3()
    
    rotMatrix26.Xx = 0.95991042373593505
    rotMatrix26.Xy = 0.24054946503154595
    rotMatrix26.Xz = -0.14390251309875576
    rotMatrix26.Yx = 0.0513956195188267
    rotMatrix26.Yy = 0.35363090577833989
    rotMatrix26.Yz = 0.93397198714558349
    rotMatrix26.Zx = 0.27555483791321111
    rotMatrix26.Zy = -0.90392540474943672
    rotMatrix26.Zz = 0.32709080383158934
    translation26 = NXOpen.Point3d(-9.6533384859372067, -3.2281853307446187, 2.6286596375574689)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix26, translation26, 6.5337666840518027)
    
    extrudeBuilder7.Destroy()
    
    section7.Destroy()
    
    workPart.Expressions.Delete(expression89)
    
    theSession.UndoToMark(markId161, None)
    
    theSession.DeleteUndoMark(markId161, None)
    
    markId162 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects8 = [NXOpen.DisplayableObject.Null] * 3 
    objects8[0] = arc3
    objects8[1] = arc2
    objects8[2] = sketch6
    theSession.DisplayManager.BlankObjects(objects8)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    rotMatrix27 = NXOpen.Matrix3x3()
    
    rotMatrix27.Xx = 0.88185465788056183
    rotMatrix27.Xy = -0.45176931596836872
    rotMatrix27.Xz = -0.13504387258900777
    rotMatrix27.Yx = 0.31140796933812004
    rotMatrix27.Yy = 0.34295459314313659
    rotMatrix27.Yz = 0.88623203715208754
    rotMatrix27.Zx = -0.35405852483321509
    rotMatrix27.Zy = -0.82358158806004655
    rotMatrix27.Zz = 0.44312067069978667
    translation27 = NXOpen.Point3d(-10.266305083778192, -1.1296323381112474, -2.454267036593901)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix27, translation27, 6.5337666840518027)
    
    rotMatrix28 = NXOpen.Matrix3x3()
    
    rotMatrix28.Xx = 0.97159668695138279
    rotMatrix28.Xy = -0.21820813105659895
    rotMatrix28.Xz = 0.091570134027879044
    rotMatrix28.Yx = -0.04551485026297853
    rotMatrix28.Yy = 0.20741515000235622
    rotMatrix28.Yz = 0.97719361129462978
    rotMatrix28.Zx = -0.23222462468617791
    rotMatrix28.Zy = -0.95360587618275916
    rotMatrix28.Zz = 0.19159216215460712
    translation28 = NXOpen.Point3d(-10.297957802086071, -4.0894232590264981, -0.75831642385111842)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix28, translation28, 6.5337666840518027)
    
    # ----------------------------------------------
    #   Menu: File->Save
    # ----------------------------------------------
    markId163 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId163, "Name Parts Dialog")
    
    markId164 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Name Parts")
    
    theSession.DeleteUndoMark(markId164, None)
    
    markId165 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Name Parts")
    
    workPart.AssignPermanentName("C:\\Users\\Admin\\Desktop\\機器人組裝\車一.prt\\車一.prt")
    
    theSession.DeleteUndoMark(markId165, None)
    
    theSession.SetUndoMarkName(markId163, "Name Parts")
    
    partSaveStatus1 = workPart.Save(NXOpen.BasePart.SaveComponents.TrueValue, NXOpen.BasePart.CloseAfterSave.FalseValue)
    
    partSaveStatus1.Dispose()
    rotMatrix29 = NXOpen.Matrix3x3()
    
    rotMatrix29.Xx = 0.78229461329318783
    rotMatrix29.Xy = -0.54990281573128452
    rotMatrix29.Xz = 0.29261242499809831
    rotMatrix29.Yx = 0.2043048718625044
    rotMatrix29.Yy = 0.67027588815983175
    rotMatrix29.Yz = 0.71343517791373068
    rotMatrix29.Zx = -0.58845106622871257
    rotMatrix29.Zy = -0.49833435262116521
    rotMatrix29.Zz = 0.63670104103255321
    translation29 = NXOpen.Point3d(-12.342919080614275, -1.3955467012678282, -4.8142019498465727)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix29, translation29, 6.5337666840518027)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()