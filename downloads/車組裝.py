# NX 1872
# Journal created by Admin on Thu Jun 20 17:38:32 2024 台北標準時間

#
import math
import NXOpen
import NXOpen.Assemblies
import NXOpen.Assemblies.ProductInterface
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.PDM
import NXOpen.Positioning
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    # ----------------------------------------------
    #   Menu: File->New...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    fileNew1 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId1, "New Dialog")
    
    fileNew1.Destroy()
    
    theSession.UndoToMark(markId1, None)
    
    theSession.DeleteUndoMark(markId1, None)
    
    # ----------------------------------------------
    #   Menu: File->New...
    # ----------------------------------------------
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    fileNew2 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId2, "New Dialog")
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    theSession.DeleteUndoMark(markId3, None)
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New")
    
    fileNew2.TemplateFileName = "assembly-mm-template.prt"
    
    fileNew2.UseBlankTemplate = False
    
    fileNew2.ApplicationName = "AssemblyTemplate"
    
    fileNew2.Units = NXOpen.Part.Units.Millimeters
    
    fileNew2.RelationType = ""
    
    fileNew2.UsesMasterModel = "No"
    
    fileNew2.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew2.TemplatePresentationName = "Assembly"
    
    fileNew2.ItemType = ""
    
    fileNew2.Specialization = ""
    
    fileNew2.SetCanCreateAltrep(False)
    
    fileNew2.NewFileName = "C:\\Users\\Admin\\Desktop\\機器人組裝\assembly1\\assembly1.prt"
    
    fileNew2.MasterFileName = ""
    
    fileNew2.MakeDisplayedPart = True
    
    fileNew2.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    # User Function call - UF_PART_ask_part_name
    
    nXObject1 = fileNew2.Commit()
    
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    theSession.DeleteUndoMark(markId4, None)
    
    fileNew2.Destroy()
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder1 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner1 = workPart.ComponentAssembly.Positioner
    
    componentPositioner1.ClearNetwork()
    
    componentPositioner1.BeginAssemblyConstraints()
    
    allowInterpartPositioning1 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    unit2 = workPart.UnitCollection.FindObject("Degrees")
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression8 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network1 = componentPositioner1.EstablishNetwork()
    
    componentNetwork1 = network1
    componentNetwork1.MoveObjectsState = True
    
    componentNetwork1.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId5, "Add Component Dialog")
    
    componentNetwork1.MoveObjectsState = True
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder1.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder1.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder1.SetCount(1)
    
    addComponentBuilder1.SetScatterOption(True)
    
    addComponentBuilder1.ReferenceSet = "Unknown"
    
    addComponentBuilder1.Layer = -1
    
    # ----------------------------------------------
    #   Dialog Begin Add Component
    # ----------------------------------------------
    scaleAboutPoint1 = NXOpen.Point3d(23.878165486579427, 3.0613032675101914, 0.0)
    viewCenter1 = NXOpen.Point3d(-23.878165486579427, -3.0613032675101914, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(19.102532389263541, 2.4490426140081532, 0.0)
    viewCenter2 = NXOpen.Point3d(-19.102532389263541, -2.4490426140081532, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(15.282025911410832, 1.9592340912065225, 0.0)
    viewCenter3 = NXOpen.Point3d(-15.282025911410832, -1.9592340912065225, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(17.878011082259476, 2.2041383526073317, 0.0)
    viewCenter4 = NXOpen.Point3d(-17.878011082259476, -2.2041383526073317, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(18.980080258563095, 0.30613032675102692, 0.0)
    viewCenter5 = NXOpen.Point3d(-18.980080258563095, -0.30613032675102692, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(22.959774506326369, 0.382662908438751, 0.0)
    viewCenter6 = NXOpen.Point3d(-22.959774506326369, -0.38266290843881628, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(28.699718132907957, 0.47832863554843874, 0.0)
    viewCenter7 = NXOpen.Point3d(-28.699718132907957, -0.47832863554852034, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(63.378544210171704, 5.9791079443557908, 0.0)
    viewCenter8 = NXOpen.Point3d(-63.378544210171704, -5.9791079443558921, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(50.702835368137364, 4.7832863554846323, 0.0)
    viewCenter9 = NXOpen.Point3d(-50.702835368137364, -4.783286355484714, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint9, viewCenter9)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Components->Add Component...
    # ----------------------------------------------
    componentPositioner1.ClearNetwork()
    
    addComponentBuilder1.RemoveAddedComponents()
    
    addComponentBuilder1.Destroy()
    
    componentPositioner1.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner1.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId6, None)
    
    theSession.UndoToMark(markId5, None)
    
    theSession.DeleteUndoMark(markId5, None)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder2 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner2 = workPart.ComponentAssembly.Positioner
    
    componentPositioner2.ClearNetwork()
    
    componentPositioner2.BeginAssemblyConstraints()
    
    allowInterpartPositioning2 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression9 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    unit3 = workPart.UnitCollection.FindObject("MilliMeter")
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    unit4 = workPart.UnitCollection.FindObject("Degrees")
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression13 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression14 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression16 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network2 = componentPositioner2.EstablishNetwork()
    
    componentNetwork2 = network2
    componentNetwork2.MoveObjectsState = True
    
    componentNetwork2.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId7, "Add Component Dialog")
    
    componentNetwork2.MoveObjectsState = True
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder2.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder2.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder2.SetCount(1)
    
    addComponentBuilder2.SetScatterOption(True)
    
    addComponentBuilder2.ReferenceSet = "Unknown"
    
    addComponentBuilder2.Layer = -1
    
    basePart1, partLoadStatus1 = theSession.Parts.OpenBase("C:\\Users\\Admin\\Desktop\\機器人組裝\車一.prt\\車一.prt")
    
    partLoadStatus1.Dispose()
    addComponentBuilder2.ReferenceSet = "Use Model"
    
    addComponentBuilder2.Layer = -1
    
    partstouse1 = [NXOpen.BasePart.Null] * 1 
    part1 = basePart1
    partstouse1[0] = part1
    addComponentBuilder2.SetPartsToAdd(partstouse1)
    
    productinterfaceobjects1 = addComponentBuilder2.GetAllProductInterfaceObjects()
    
    arrangement1 = workPart.ComponentAssembly.Arrangements.FindObject("Arrangement 1")
    componentPositioner2.PrimaryArrangement = arrangement1
    
    scaleAboutPoint10 = NXOpen.Point3d(1.5306516337550691, 3.4439661759489217, 0.0)
    viewCenter10 = NXOpen.Point3d(-1.5306516337550691, -3.443966175948987, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(1.2245213070040553, 2.7551729407591377, 0.0)
    viewCenter11 = NXOpen.Point3d(-1.2245213070040553, -2.7551729407591896, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(0.97961704560326501, 2.2041383526073099, 0.0)
    viewCenter12 = NXOpen.Point3d(-0.97961704560326501, -2.2041383526073308, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(0.78369363648259527, 1.7633106820858477, 0.0)
    viewCenter13 = NXOpen.Point3d(-0.78369363648259527, -1.7633106820858813, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(1.3364347691139182e-14, 0.15673872729651236, 0.0)
    viewCenter14 = NXOpen.Point3d(1.3364347691139182e-14, -0.15673872729653909, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(-1.7554737457210348, -2.3824286549071378, 0.0)
    viewCenter15 = NXOpen.Point3d(1.7554737457210563, 2.3824286549071059, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(-1.7053173529861403, -2.3071940658048078, 0.0)
    viewCenter16 = NXOpen.Point3d(1.7053173529861745, 2.307194065804782, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint16, viewCenter16)
    
    scaleAboutPoint17 = NXOpen.Point3d(-1.3642538823889054, -1.8457552526438463, 0.0)
    viewCenter17 = NXOpen.Point3d(1.3642538823889396, 1.8457552526438121, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint17, viewCenter17)
    
    coordinates1 = NXOpen.Point3d(-0.96196669530002787, 1.4558946256072585, 0.0)
    point1 = workPart.Points.CreatePoint(coordinates1)
    
    coordinates2 = NXOpen.Point3d(-0.96196669530002787, 1.4558946256072585, 0.0)
    point2 = workPart.Points.CreatePoint(coordinates2)
    
    origin1 = NXOpen.Point3d(-0.96196669530002787, 1.4558946256072585, 0.0)
    vector1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction1 = workPart.Directions.CreateDirection(origin1, vector1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin2 = NXOpen.Point3d(-0.96196669530002787, 1.4558946256072585, 0.0)
    vector2 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction2 = workPart.Directions.CreateDirection(origin2, vector2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin3 = NXOpen.Point3d(-0.96196669530002787, 1.4558946256072585, 0.0)
    matrix1 = NXOpen.Matrix3x3()
    
    matrix1.Xx = 1.0
    matrix1.Xy = 0.0
    matrix1.Xz = 0.0
    matrix1.Yx = 0.0
    matrix1.Yy = 1.0
    matrix1.Yz = 0.0
    matrix1.Zx = 0.0
    matrix1.Zy = 0.0
    matrix1.Zz = 1.0
    plane1 = workPart.Planes.CreateFixedTypePlane(origin3, matrix1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane1, direction2, point2, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point3 = NXOpen.Point3d(-0.96196669530002787, 1.4558946256072585, 0.0)
    orientation1 = NXOpen.Matrix3x3()
    
    orientation1.Xx = 1.0
    orientation1.Xy = 0.0
    orientation1.Xz = 0.0
    orientation1.Yx = 0.0
    orientation1.Yy = 1.0
    orientation1.Yz = 0.0
    orientation1.Zx = 0.0
    orientation1.Zy = 0.0
    orientation1.Zz = 1.0
    addComponentBuilder2.SetInitialLocationAndOrientation(point3, orientation1)
    
    movableObjects1 = [NXOpen.NXObject.Null] * 1 
    component1 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 車一 1")
    movableObjects1[0] = component1
    componentNetwork2.SetMovingGroup(movableObjects1)
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    theSession.DeleteUndoMark(markId9, None)
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork2.Solve()
    
    componentPositioner2.ClearNetwork()
    
    nErrs1 = theSession.UpdateManager.AddToDeleteList(componentNetwork2)
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId8)
    
    componentPositioner2.EndAssemblyConstraints()
    
    logicalobjects1 = addComponentBuilder2.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder2.ComponentName = "車一"
    
    nXObject2 = addComponentBuilder2.Commit()
    
    errorList1 = addComponentBuilder2.GetOperationFailures()
    
    errorList1.Dispose()
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "ComponentOperationUtilities CreateFixConstraint")
    
    componentPositioner3 = workPart.ComponentAssembly.Positioner
    
    componentPositioner3.ClearNetwork()
    
    network3 = componentPositioner3.EstablishNetwork()
    
    componentNetwork3 = network3
    componentNetwork3.MoveObjectsState = True
    
    componentNetwork3.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork3.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    constraint1 = componentPositioner3.CreateConstraint(True)
    
    componentConstraint1 = constraint1
    componentConstraint1.ConstraintType = NXOpen.Positioning.Constraint.Type.Fix
    
    component2 = nXObject2
    constraintReference1 = componentConstraint1.CreateConstraintReference(component2, component2, False, False, False)
    
    componentNetwork3.Solve()
    
    componentPositioner3.ClearNetwork()
    
    nErrs3 = theSession.UpdateManager.AddToDeleteList(componentNetwork3)
    
    nErrs4 = theSession.UpdateManager.DoUpdate(markId7)
    
    theSession.DeleteUndoMark(markId10, None)
    
    theSession.SetUndoMarkName(markId7, "Add Component")
    
    addComponentBuilder2.Destroy()
    
    workPart.Points.DeletePoint(point1)
    
    componentPositioner3.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId8, None)
    
    scaleAboutPoint18 = NXOpen.Point3d(-8.410223933785808, 0.32100091350326282, 0.0)
    viewCenter18 = NXOpen.Point3d(8.4102239337858347, -0.32100091350329019, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint18, viewCenter18)
    
    scaleAboutPoint19 = NXOpen.Point3d(-10.03127854697736, 0.40125114187908534, 0.0)
    viewCenter19 = NXOpen.Point3d(10.031278546977372, -0.40125114187911953, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(-12.539098183721691, 0.50156392734885669, 0.0)
    viewCenter20 = NXOpen.Point3d(12.539098183721725, -0.50156392734888233, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(-10.031278546977353, 0.40125114187908534, 0.0)
    viewCenter21 = NXOpen.Point3d(10.031278546977379, -0.40125114187911953, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint21, viewCenter21)
    
    scaleAboutPoint22 = NXOpen.Point3d(-8.0250228375818704, 0.32100091350326276, 0.0)
    viewCenter22 = NXOpen.Point3d(8.0250228375819148, -0.32100091350329013, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(-6.4200182700655013, 0.25680073080260585, 0.0)
    viewCenter23 = NXOpen.Point3d(6.4200182700655271, -0.25680073080263649, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint23, viewCenter23)
    
    scaleAboutPoint24 = NXOpen.Point3d(-5.1360146160523978, 0.2054405846420812, 0.0)
    viewCenter24 = NXOpen.Point3d(5.1360146160524254, -0.20544058464211273, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint24, viewCenter24)
    
    scaleAboutPoint25 = NXOpen.Point3d(-4.1088116928419209, 0.16435246771366493, 0.0)
    viewCenter25 = NXOpen.Point3d(4.1088116928419378, -0.16435246771369297, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint25, viewCenter25)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Components->Add Component...
    # ----------------------------------------------
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder3 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner4 = workPart.ComponentAssembly.Positioner
    
    componentPositioner4.ClearNetwork()
    
    componentPositioner4.PrimaryArrangement = arrangement1
    
    componentPositioner4.BeginAssemblyConstraints()
    
    allowInterpartPositioning3 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression17 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression18 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression19 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression20 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression23 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression24 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network4 = componentPositioner4.EstablishNetwork()
    
    componentNetwork4 = network4
    componentNetwork4.MoveObjectsState = True
    
    componentNetwork4.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId13, "Add Component Dialog")
    
    componentNetwork4.MoveObjectsState = True
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder3.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder3.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder3.SetCount(1)
    
    addComponentBuilder3.SetScatterOption(True)
    
    addComponentBuilder3.ReferenceSet = "Unknown"
    
    addComponentBuilder3.Layer = -1
    
    basePart2, partLoadStatus2 = theSession.Parts.OpenBase("C:\\Users\\Admin\\Desktop\\機器人組裝\車三.prt\\車三.prt")
    
    partLoadStatus2.Dispose()
    addComponentBuilder3.ReferenceSet = "Use Model"
    
    addComponentBuilder3.Layer = -1
    
    partstouse2 = [NXOpen.BasePart.Null] * 1 
    part2 = basePart2
    partstouse2[0] = part2
    addComponentBuilder3.SetPartsToAdd(partstouse2)
    
    productinterfaceobjects2 = addComponentBuilder3.GetAllProductInterfaceObjects()
    
    coordinates3 = NXOpen.Point3d(-6.9685169658111894, -7.9961545986186096, 0.0)
    point4 = workPart.Points.CreatePoint(coordinates3)
    
    coordinates4 = NXOpen.Point3d(-6.9685169658111894, -7.9961545986186096, 0.0)
    point5 = workPart.Points.CreatePoint(coordinates4)
    
    origin4 = NXOpen.Point3d(-6.9685169658111894, -7.9961545986186096, 0.0)
    vector3 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction3 = workPart.Directions.CreateDirection(origin4, vector3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin5 = NXOpen.Point3d(-6.9685169658111894, -7.9961545986186096, 0.0)
    vector4 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction4 = workPart.Directions.CreateDirection(origin5, vector4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin6 = NXOpen.Point3d(-6.9685169658111894, -7.9961545986186096, 0.0)
    matrix2 = NXOpen.Matrix3x3()
    
    matrix2.Xx = 1.0
    matrix2.Xy = 0.0
    matrix2.Xz = 0.0
    matrix2.Yx = 0.0
    matrix2.Yy = 1.0
    matrix2.Yz = 0.0
    matrix2.Zx = 0.0
    matrix2.Zy = 0.0
    matrix2.Zz = 1.0
    plane2 = workPart.Planes.CreateFixedTypePlane(origin6, matrix2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane2, direction4, point5, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point6 = NXOpen.Point3d(-6.9685169658111894, -7.9961545986186096, 0.0)
    orientation2 = NXOpen.Matrix3x3()
    
    orientation2.Xx = 1.0
    orientation2.Xy = 0.0
    orientation2.Xz = 0.0
    orientation2.Yx = 0.0
    orientation2.Yy = 1.0
    orientation2.Yz = 0.0
    orientation2.Zx = 0.0
    orientation2.Zy = 0.0
    orientation2.Zz = 1.0
    addComponentBuilder3.SetInitialLocationAndOrientation(point6, orientation2)
    
    movableObjects2 = [NXOpen.NXObject.Null] * 1 
    component3 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 車三 1")
    movableObjects2[0] = component3
    componentNetwork4.SetMovingGroup(movableObjects2)
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork4.Solve()
    
    componentPositioner4.ClearNetwork()
    
    nErrs5 = theSession.UpdateManager.AddToDeleteList(componentNetwork4)
    
    nErrs6 = theSession.UpdateManager.DoUpdate(markId14)
    
    componentPositioner4.EndAssemblyConstraints()
    
    logicalobjects2 = addComponentBuilder3.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder3.ComponentName = "車三"
    
    nXObject3 = addComponentBuilder3.Commit()
    
    errorList2 = addComponentBuilder3.GetOperationFailures()
    
    errorList2.Dispose()
    theSession.DeleteUndoMark(markId15, None)
    
    theSession.SetUndoMarkName(markId13, "Add Component")
    
    addComponentBuilder3.Destroy()
    
    workPart.Points.DeletePoint(point4)
    
    componentPositioner4.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId14, None)
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder4 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner5 = workPart.ComponentAssembly.Positioner
    
    componentPositioner5.ClearNetwork()
    
    componentPositioner5.PrimaryArrangement = arrangement1
    
    componentPositioner5.BeginAssemblyConstraints()
    
    allowInterpartPositioning4 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression25 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression26 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression28 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression31 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression32 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network5 = componentPositioner5.EstablishNetwork()
    
    componentNetwork5 = network5
    componentNetwork5.MoveObjectsState = True
    
    componentNetwork5.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId17, "Add Component Dialog")
    
    componentNetwork5.MoveObjectsState = True
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder4.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder4.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder4.SetCount(1)
    
    addComponentBuilder4.SetScatterOption(True)
    
    addComponentBuilder4.ReferenceSet = "Unknown"
    
    addComponentBuilder4.Layer = -1
    
    # ----------------------------------------------
    #   Dialog Begin Add Component
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Assemblies->Components->Add Component...
    # ----------------------------------------------
    componentPositioner5.ClearNetwork()
    
    addComponentBuilder4.RemoveAddedComponents()
    
    addComponentBuilder4.Destroy()
    
    componentPositioner5.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner5.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId18, None)
    
    theSession.UndoToMark(markId17, None)
    
    theSession.DeleteUndoMark(markId17, None)
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder5 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner6 = workPart.ComponentAssembly.Positioner
    
    componentPositioner6.ClearNetwork()
    
    componentPositioner6.PrimaryArrangement = arrangement1
    
    componentPositioner6.BeginAssemblyConstraints()
    
    allowInterpartPositioning5 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression33 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression34 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression35 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression36 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression37 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression38 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression39 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression40 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network6 = componentPositioner6.EstablishNetwork()
    
    componentNetwork6 = network6
    componentNetwork6.MoveObjectsState = True
    
    componentNetwork6.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId19, "Add Component Dialog")
    
    componentNetwork6.MoveObjectsState = True
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder5.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder5.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder5.SetCount(1)
    
    addComponentBuilder5.SetScatterOption(True)
    
    addComponentBuilder5.ReferenceSet = "Unknown"
    
    addComponentBuilder5.Layer = -1
    
    addComponentBuilder5.ReferenceSet = "Use Model"
    
    addComponentBuilder5.Layer = -1
    
    partstouse3 = [NXOpen.BasePart.Null] * 1 
    partstouse3[0] = part2
    addComponentBuilder5.SetPartsToAdd(partstouse3)
    
    productinterfaceobjects3 = addComponentBuilder5.GetAllProductInterfaceObjects()
    
    coordinates5 = NXOpen.Point3d(-0.88244613736328414, -9.7283340944193988, 0.0)
    point7 = workPart.Points.CreatePoint(coordinates5)
    
    coordinates6 = NXOpen.Point3d(-0.88244613736328414, -9.7283340944193988, 0.0)
    point8 = workPart.Points.CreatePoint(coordinates6)
    
    origin7 = NXOpen.Point3d(-0.88244613736328414, -9.7283340944193988, 0.0)
    vector5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction5 = workPart.Directions.CreateDirection(origin7, vector5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin8 = NXOpen.Point3d(-0.88244613736328414, -9.7283340944193988, 0.0)
    vector6 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction6 = workPart.Directions.CreateDirection(origin8, vector6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin9 = NXOpen.Point3d(-0.88244613736328414, -9.7283340944193988, 0.0)
    matrix3 = NXOpen.Matrix3x3()
    
    matrix3.Xx = 1.0
    matrix3.Xy = 0.0
    matrix3.Xz = 0.0
    matrix3.Yx = 0.0
    matrix3.Yy = 1.0
    matrix3.Yz = 0.0
    matrix3.Zx = 0.0
    matrix3.Zy = 0.0
    matrix3.Zz = 1.0
    plane3 = workPart.Planes.CreateFixedTypePlane(origin9, matrix3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform3 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane3, direction6, point8, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem3 = workPart.CoordinateSystems.CreateCoordinateSystem(xform3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point9 = NXOpen.Point3d(-0.88244613736328414, -9.7283340944193988, 0.0)
    orientation3 = NXOpen.Matrix3x3()
    
    orientation3.Xx = 1.0
    orientation3.Xy = 0.0
    orientation3.Xz = 0.0
    orientation3.Yx = 0.0
    orientation3.Yy = 1.0
    orientation3.Yz = 0.0
    orientation3.Zx = 0.0
    orientation3.Zy = 0.0
    orientation3.Zz = 1.0
    addComponentBuilder5.SetInitialLocationAndOrientation(point9, orientation3)
    
    movableObjects3 = [NXOpen.NXObject.Null] * 1 
    component4 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 車三 1")
    movableObjects3[0] = component4
    componentNetwork6.SetMovingGroup(movableObjects3)
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork6.Solve()
    
    componentPositioner6.ClearNetwork()
    
    nErrs7 = theSession.UpdateManager.AddToDeleteList(componentNetwork6)
    
    nErrs8 = theSession.UpdateManager.DoUpdate(markId20)
    
    componentPositioner6.EndAssemblyConstraints()
    
    logicalobjects3 = addComponentBuilder5.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder5.ComponentName = "車三"
    
    nXObject4 = addComponentBuilder5.Commit()
    
    errorList3 = addComponentBuilder5.GetOperationFailures()
    
    errorList3.Dispose()
    theSession.DeleteUndoMark(markId21, None)
    
    theSession.SetUndoMarkName(markId19, "Add Component")
    
    addComponentBuilder5.Destroy()
    
    workPart.Points.DeletePoint(point7)
    
    componentPositioner6.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId20, None)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder6 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner7 = workPart.ComponentAssembly.Positioner
    
    componentPositioner7.ClearNetwork()
    
    componentPositioner7.PrimaryArrangement = arrangement1
    
    componentPositioner7.BeginAssemblyConstraints()
    
    allowInterpartPositioning6 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression41 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression42 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression43 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression44 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression45 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression46 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression47 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression48 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network7 = componentPositioner7.EstablishNetwork()
    
    componentNetwork7 = network7
    componentNetwork7.MoveObjectsState = True
    
    componentNetwork7.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId23, "Add Component Dialog")
    
    componentNetwork7.MoveObjectsState = True
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder6.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder6.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder6.SetCount(1)
    
    addComponentBuilder6.SetScatterOption(True)
    
    addComponentBuilder6.ReferenceSet = "Unknown"
    
    addComponentBuilder6.Layer = -1
    
    # ----------------------------------------------
    #   Dialog Begin Add Component
    # ----------------------------------------------
    componentPositioner7.ClearNetwork()
    
    addComponentBuilder6.RemoveAddedComponents()
    
    addComponentBuilder6.Destroy()
    
    componentPositioner7.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner7.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId24, None)
    
    theSession.UndoToMark(markId23, None)
    
    theSession.DeleteUndoMark(markId23, None)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner8 = workPart.ComponentAssembly.Positioner
    
    componentPositioner8.ClearNetwork()
    
    componentPositioner8.PrimaryArrangement = arrangement1
    
    componentPositioner8.BeginAssemblyConstraints()
    
    allowInterpartPositioning7 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression49 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression50 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression51 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression52 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression53 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression54 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression55 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression56 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network8 = componentPositioner8.EstablishNetwork()
    
    componentNetwork8 = network8
    componentNetwork8.MoveObjectsState = True
    
    componentNetwork8.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork8.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId26, "Assembly Constraints Dialog")
    
    componentNetwork8.MoveObjectsState = True
    
    componentNetwork8.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    component5 = nXObject3
    face1 = component5.FindObject("PROTO#.Features|REVOLVED(1)|FACE 1")
    line1 = workPart.Lines.CreateFaceAxis(face1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line1.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    face2 = component2.FindObject("PROTO#.Features|EXTRUDE(7)|FACE 140 {(-12.2999999999998,0,0.8236909777065) EXTRUDE(2)}")
    line2 = workPart.Lines.CreateFaceAxis(face2, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line2.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint2 = componentPositioner8.CreateConstraint(True)
    
    componentConstraint2 = constraint2
    componentConstraint2.ConstraintType = NXOpen.Positioning.Constraint.Type.Distance
    
    constraintReference2 = componentConstraint2.CreateConstraintReference(component5, face1, True, False, False)
    
    helpPoint1 = NXOpen.Point3d(-6.9685169658111885, -9.0306626360127389, -3.6082248300317588e-16)
    constraintReference2.HelpPoint = helpPoint1
    
    constraintReference3 = componentConstraint2.CreateConstraintReference(component2, face2, True, False, False)
    
    helpPoint2 = NXOpen.Point3d(-13.261966695299856, -2.4886585206944032, 0.52369097770650797)
    constraintReference3.HelpPoint = helpPoint2
    
    constraintReference3.SetFixHint(True)
    
    componentConstraint2.SetExpression("0")
    
    componentConstraint2.SetExpression("6.31520084698279")
    
    objects1 = [NXOpen.TaggedObject.Null] * 1 
    objects1[0] = line2
    nErrs9 = theSession.UpdateManager.AddObjectsToDeleteList(objects1)
    
    objects2 = [NXOpen.TaggedObject.Null] * 1 
    objects2[0] = line1
    nErrs10 = theSession.UpdateManager.AddObjectsToDeleteList(objects2)
    
    componentNetwork8.Solve()
    
    componentNetwork8.Solve()
    
    componentPositioner8.ClearNetwork()
    
    nErrs11 = theSession.UpdateManager.AddToDeleteList(componentNetwork8)
    
    componentPositioner8.DeleteNonPersistentConstraints()
    
    nErrs12 = theSession.UpdateManager.DoUpdate(markId27)
    
    theSession.SetUndoMarkName(markId26, "Assembly Constraints")
    
    componentPositioner8.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner8.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId27, None)
    
    theSession.DeleteUndoMark(markId28, None)
    
    theSession.DeleteUndoMark(markId25, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Undo
    # ----------------------------------------------
    marksRecycled1, undoUnavailable1 = theSession.UndoLastNVisibleMarks(1)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner9 = workPart.ComponentAssembly.Positioner
    
    componentPositioner9.ClearNetwork()
    
    componentPositioner9.PrimaryArrangement = arrangement1
    
    componentPositioner9.BeginAssemblyConstraints()
    
    allowInterpartPositioning8 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression57 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression58 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression59 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression60 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression61 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression62 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression63 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression64 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network9 = componentPositioner9.EstablishNetwork()
    
    componentNetwork9 = network9
    componentNetwork9.MoveObjectsState = True
    
    componentNetwork9.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork9.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId30, "Assembly Constraints Dialog")
    
    componentNetwork9.MoveObjectsState = True
    
    componentNetwork9.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    line3 = workPart.Lines.CreateFaceAxis(face1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line3.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    line4 = workPart.Lines.CreateFaceAxis(face2, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line4.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint3 = componentPositioner9.CreateConstraint(True)
    
    componentConstraint3 = constraint3
    componentConstraint3.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.CoAlign
    
    componentConstraint3.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    constraintReference4 = componentConstraint3.CreateConstraintReference(component5, face1, True, False, False)
    
    helpPoint3 = NXOpen.Point3d(-6.9685169658111876, -8.9807041349405115, -8.3266726846886741e-17)
    constraintReference4.HelpPoint = helpPoint3
    
    constraintReference5 = componentConstraint3.CreateConstraintReference(component2, face2, True, False, False)
    
    helpPoint4 = NXOpen.Point3d(-13.261966695299854, -2.5885755228388465, 0.52369097770650841)
    constraintReference5.HelpPoint = helpPoint4
    
    constraintReference5.SetFixHint(True)
    
    objects3 = [NXOpen.TaggedObject.Null] * 1 
    objects3[0] = line4
    nErrs13 = theSession.UpdateManager.AddObjectsToDeleteList(objects3)
    
    objects4 = [NXOpen.TaggedObject.Null] * 1 
    objects4[0] = line3
    nErrs14 = theSession.UpdateManager.AddObjectsToDeleteList(objects4)
    
    componentNetwork9.Solve()
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs15 = theSession.UpdateManager.DoUpdate(markId31)
    
    componentNetwork9.Solve()
    
    componentPositioner9.ClearNetwork()
    
    nErrs16 = theSession.UpdateManager.AddToDeleteList(componentNetwork9)
    
    componentPositioner9.DeleteNonPersistentConstraints()
    
    nErrs17 = theSession.UpdateManager.DoUpdate(markId31)
    
    theSession.DeleteUndoMark(markId33, None)
    
    theSession.SetUndoMarkName(markId30, "Assembly Constraints")
    
    componentPositioner9.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner9.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId31, None)
    
    theSession.DeleteUndoMark(markId32, None)
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner10 = workPart.ComponentAssembly.Positioner
    
    componentPositioner10.ClearNetwork()
    
    componentPositioner10.PrimaryArrangement = arrangement1
    
    componentPositioner10.BeginAssemblyConstraints()
    
    allowInterpartPositioning9 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression65 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression66 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression67 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression68 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression69 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression70 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression71 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression72 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network10 = componentPositioner10.EstablishNetwork()
    
    componentNetwork10 = network10
    componentNetwork10.MoveObjectsState = True
    
    componentNetwork10.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork10.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId34, "Assembly Constraints Dialog")
    
    componentNetwork10.MoveObjectsState = True
    
    componentNetwork10.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   Dialog Begin Assembly Constraints
    # ----------------------------------------------
    scaleAboutPoint26 = NXOpen.Point3d(-12.12263801856081, -0.10518557933676752, 0.0)
    viewCenter26 = NXOpen.Point3d(12.122638018560833, 0.10518557933673837, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint26, viewCenter26)
    
    scaleAboutPoint27 = NXOpen.Point3d(-9.6981104148486459, -0.084148463469415805, 0.0)
    viewCenter27 = NXOpen.Point3d(9.6981104148486672, 0.084148463469387105, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint27, viewCenter27)
    
    scaleAboutPoint28 = NXOpen.Point3d(-12.122638018560808, -0.10518557933676526, 0.0)
    viewCenter28 = NXOpen.Point3d(12.122638018560831, 0.10518557933673836, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint28, viewCenter28)
    
    line5 = workPart.Lines.CreateFaceAxis(face1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line5.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    face3 = component5.FindObject("PROTO#.Features|BLEND(2)|FACE 2 {(0,-7.9707106781187,-0.2707106781187) REVOLVED(1)}")
    line6 = workPart.Lines.CreateFaceAxis(face3, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line6.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint29 = NXOpen.Point3d(-24.554258676423338, -2.4324165221624332, 0.0)
    viewCenter29 = NXOpen.Point3d(24.554258676423363, 2.4324165221624052, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint29, viewCenter29)
    
    scaleAboutPoint30 = NXOpen.Point3d(-19.643406941138668, -1.9459332177299489, 0.0)
    viewCenter30 = NXOpen.Point3d(19.643406941138689, 1.945933217729922, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint30, viewCenter30)
    
    scaleAboutPoint31 = NXOpen.Point3d(-15.714725552910938, -1.5567465741839632, 0.0)
    viewCenter31 = NXOpen.Point3d(15.714725552910956, 1.5567465741839346, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(-12.50446167155323, -1.2453972593471734, 0.0)
    viewCenter32 = NXOpen.Point3d(12.504461671553242, 1.2453972593471447, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(-10.003569337242583, -0.99631780747774079, 0.0)
    viewCenter33 = NXOpen.Point3d(10.00356933724259, 0.99631780747771204, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint33, viewCenter33)
    
    scaleAboutPoint34 = NXOpen.Point3d(-7.9920844664699828, -0.79705424598219632, 0.0)
    viewCenter34 = NXOpen.Point3d(7.9920844664699899, 0.79705424598216779, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint34, viewCenter34)
    
    objects5 = [NXOpen.TaggedObject.Null] * 1 
    objects5[0] = line6
    nErrs18 = theSession.UpdateManager.AddObjectsToDeleteList(objects5)
    
    objects6 = [NXOpen.TaggedObject.Null] * 1 
    objects6[0] = line5
    nErrs19 = theSession.UpdateManager.AddObjectsToDeleteList(objects6)
    
    scaleAboutPoint35 = NXOpen.Point3d(-3.5587394982771987, -0.025850407977815192, 0.0)
    viewCenter35 = NXOpen.Point3d(3.5587394982772063, 0.025850407977785806, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint35, viewCenter35)
    
    scaleAboutPoint36 = NXOpen.Point3d(-4.4484243728464987, -0.032313009972264391, 0.0)
    viewCenter36 = NXOpen.Point3d(4.4484243728465076, 0.03231300997223592, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint36, viewCenter36)
    
    scaleAboutPoint37 = NXOpen.Point3d(-5.5605304660581227, -0.040391262465325886, 0.0)
    viewCenter37 = NXOpen.Point3d(5.560530466058129, 0.040391262465299484, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint37, viewCenter37)
    
    scaleAboutPoint38 = NXOpen.Point3d(-6.9506630825726532, -0.050489078081654475, 0.0)
    viewCenter38 = NXOpen.Point3d(6.9506630825726621, 0.050489078081628648, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint38, viewCenter38)
    
    scaleAboutPoint39 = NXOpen.Point3d(-8.6883288532158165, -0.063111347602064508, 0.0)
    viewCenter39 = NXOpen.Point3d(8.6883288532158236, 0.063111347602039389, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint39, viewCenter39)
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint4 = componentPositioner10.CreateConstraint(True)
    
    componentConstraint4 = constraint4
    componentConstraint4.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.CoAlign
    
    componentConstraint4.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    face4 = component5.FindObject("PROTO#.Features|REVOLVED(1)|FACE 3")
    constraintReference6 = componentConstraint4.CreateConstraintReference(component5, face4, False, False, False)
    
    helpPoint5 = NXOpen.Point3d(-13.252861486908152, -15.99615459865681, 0.39787541445519997)
    constraintReference6.HelpPoint = helpPoint5
    
    face5 = component2.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 130 {(-7.5,-4,2.8769308262358) EXTRUDE(2)}")
    constraintReference7 = componentConstraint4.CreateConstraintReference(component2, face5, False, False, False)
    
    helpPoint6 = NXOpen.Point3d(-12.573008686118222, -2.5441053744118407, 1.3781773161554156)
    constraintReference7.HelpPoint = helpPoint6
    
    constraintReference7.SetFixHint(True)
    
    componentNetwork10.Solve()
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = 0.58601650951901185
    rotMatrix1.Xy = 0.80864109214716751
    rotMatrix1.Xz = -0.051809600096857422
    rotMatrix1.Yx = -0.35219434763423957
    rotMatrix1.Yy = 0.31177271188288624
    rotMatrix1.Yz = 0.88247204920024769
    rotMatrix1.Zx = 0.72975598117840212
    rotMatrix1.Zy = -0.49889614171311442
    rotMatrix1.Zz = 0.46750277829989401
    translation1 = NXOpen.Point3d(7.0320078487650362, -0.9880380248094276, 0.33187046983500923)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 10.061582015392649)
    
    componentPositioner10.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner10.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId35, None)
    
    theSession.UndoToMark(markId34, None)
    
    theSession.DeleteUndoMark(markId34, None)
    
    theSession.DeleteUndoMark(markId29, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete1 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects7 = [NXOpen.TaggedObject.Null] * 1 
    objects7[0] = component5
    nErrs20 = theSession.UpdateManager.AddObjectsToDeleteList(objects7)
    
    notifyOnDelete2 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs21 = theSession.UpdateManager.DoUpdate(id1)
    
    theSession.DeleteUndoMark(markId37, None)
    
    # ----------------------------------------------
    #   Menu: Edit->Delete...
    # ----------------------------------------------
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete3 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects8 = [NXOpen.TaggedObject.Null] * 1 
    component6 = nXObject4
    objects8[0] = component6
    nErrs22 = theSession.UpdateManager.AddObjectsToDeleteList(objects8)
    
    notifyOnDelete4 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id2 = theSession.NewestVisibleUndoMark
    
    nErrs23 = theSession.UpdateManager.DoUpdate(id2)
    
    theSession.DeleteUndoMark(markId39, None)
    
    # ----------------------------------------------
    #   Menu: File->Open...
    # ----------------------------------------------
    try:
        # File already exists
        basePart3, partLoadStatus3 = theSession.Parts.OpenActiveDisplay("C:\\Users\\Admin\\Desktop\\機器人組裝\車三.prt\\車三.prt", NXOpen.DisplayPartOption.AllowAdditional)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1020004)
        
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    status1, partLoadStatus4 = theSession.Parts.SetActiveDisplay(part2, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = theSession.Parts.Work # 車三
    displayPart = theSession.Parts.Display # 車三
    partLoadStatus4.Dispose()
    scaleAboutPoint40 = NXOpen.Point3d(-1.3804016033951174, -0.52932693062518921, 0.0)
    viewCenter40 = NXOpen.Point3d(1.3804016033950848, 0.52932693062518921, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint40, viewCenter40)
    
    scaleAboutPoint41 = NXOpen.Point3d(-1.7255020042438922, -0.66165866328148648, 0.0)
    viewCenter41 = NXOpen.Point3d(1.7255020042438614, 0.66165866328148648, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint41, viewCenter41)
    
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit Parameters...
    # ----------------------------------------------
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    # User Function call - UF_PART_ask_part_name
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    revolve1 = workPart.Features.FindObject("REVOLVED(1)")
    revolveBuilder1 = workPart.Features.CreateRevolveBuilder(revolve1)
    
    section1 = revolveBuilder1.Section
    
    section1.PrepareMappingData()
    
    unit5 = revolveBuilder1.Offset.StartOffset.Units
    
    expression73 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit5)
    
    theSession.SetUndoMarkName(markId43, "Revolve Dialog")
    
    sketchFeature1 = workPart.Features.FindObject("REVOLVED(1:1B)")
    revolveBuilder1.ShowInternalParentFeatureForEdit(sketchFeature1)
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    scaleAboutPoint42 = NXOpen.Point3d(-1.8474547774761667, -0.020757918848048996, 0.0)
    viewCenter42 = NXOpen.Point3d(1.8474547774761332, 0.020757918848048996, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint42, viewCenter42)
    
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId45, None)
    
    revolveBuilder1.Section = section1
    
    workPart.Expressions.Delete(expression73)
    
    expression74 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit5)
    
    theSession.DeleteUndoMark(markId44, None)
    
    expression75 = workPart.Expressions.FindObject("p5")
    expression75.SetFormula("12")
    
    sketch1 = sketchFeature1.FindObject("SKETCH_000")
    sketch1.LocalUpdate()
    
    revolveBuilder1.Section = section1
    
    scaleAboutPoint43 = NXOpen.Point3d(1.1209276177945011, 0.074728507852967876, 0.0)
    viewCenter43 = NXOpen.Point3d(-1.1209276177945351, -0.074728507852967876, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint43, viewCenter43)
    
    scaleAboutPoint44 = NXOpen.Point3d(1.4011595222431317, 0.093410634816209842, 0.0)
    viewCenter44 = NXOpen.Point3d(-1.4011595222431643, -0.093410634816209842, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint44, viewCenter44)
    
    scaleAboutPoint45 = NXOpen.Point3d(1.7514494028039187, 0.11676329352026227, 0.0)
    viewCenter45 = NXOpen.Point3d(-1.7514494028039507, -0.11676329352026227, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint45, viewCenter45)
    
    scaleAboutPoint46 = NXOpen.Point3d(2.0433576366045729, 0.14595411690032783, 0.0)
    viewCenter46 = NXOpen.Point3d(-2.0433576366046062, -0.14595411690032783, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint46, viewCenter46)
    
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    
    theSession.DeleteUndoMark(markId46, None)
    
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    
    feature1 = revolveBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId47, None)
    
    theSession.SetUndoMarkName(markId43, "Revolve")
    
    section1.CleanMappingData()
    
    expression76 = revolveBuilder1.Limits.StartExtend.Value
    expression77 = revolveBuilder1.Limits.EndExtend.Value
    revolveBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression74)
    
    theSession.DeleteUndoMark(markId43, None)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    nErrs24 = theSession.UpdateManager.DoUpdate(markId42)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    # ----------------------------------------------
    #   Menu: File->Save
    # ----------------------------------------------
    partSaveStatus1 = workPart.Save(NXOpen.BasePart.SaveComponents.TrueValue, NXOpen.BasePart.CloseAfterSave.FalseValue)
    
    partSaveStatus1.Dispose()
    partCloseResponses1 = theSession.Parts.NewPartCloseResponses()
    
    # User Function call - UF_PART_ask_num_parts
    
    workPart.Close(NXOpen.BasePart.CloseWholeTree.FalseValue, NXOpen.BasePart.CloseModified.UseResponses, partCloseResponses1)
    
    workPart = NXOpen.Part.Null
    displayPart = NXOpen.Part.Null
    partCloseResponses1.Dispose()
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    part3 = nXObject1
    status2, partLoadStatus5 = theSession.Parts.SetActiveDisplay(part3, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = theSession.Parts.Work # assembly1
    displayPart = theSession.Parts.Display # assembly1
    partLoadStatus5.Dispose()
    # ----------------------------------------------
    #   Menu: Assemblies->Components->Add Component...
    # ----------------------------------------------
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder7 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner11 = workPart.ComponentAssembly.Positioner
    
    componentPositioner11.ClearNetwork()
    
    componentPositioner11.PrimaryArrangement = arrangement1
    
    componentPositioner11.BeginAssemblyConstraints()
    
    allowInterpartPositioning10 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression78 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression79 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression80 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression81 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression82 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression83 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression84 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression85 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network11 = componentPositioner11.EstablishNetwork()
    
    componentNetwork11 = network11
    componentNetwork11.MoveObjectsState = True
    
    componentNetwork11.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId49, "Add Component Dialog")
    
    componentNetwork11.MoveObjectsState = True
    
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder7.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder7.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder7.SetCount(1)
    
    addComponentBuilder7.SetScatterOption(True)
    
    addComponentBuilder7.ReferenceSet = "Unknown"
    
    addComponentBuilder7.Layer = -1
    
    basePart4, partLoadStatus6 = theSession.Parts.OpenBase("C:\\Users\\Admin\\Desktop\\機器人組裝\車三.prt\\車三.prt")
    
    partLoadStatus6.Dispose()
    addComponentBuilder7.ReferenceSet = "Use Model"
    
    addComponentBuilder7.Layer = -1
    
    partstouse4 = [NXOpen.BasePart.Null] * 1 
    part4 = basePart4
    partstouse4[0] = part4
    addComponentBuilder7.SetPartsToAdd(partstouse4)
    
    productinterfaceobjects4 = addComponentBuilder7.GetAllProductInterfaceObjects()
    
    coordinates7 = NXOpen.Point3d(-13.363907159494168, -6.3606993313823352, 0.0)
    point10 = workPart.Points.CreatePoint(coordinates7)
    
    coordinates8 = NXOpen.Point3d(-13.363907159494168, -6.3606993313823352, 0.0)
    point11 = workPart.Points.CreatePoint(coordinates8)
    
    origin10 = NXOpen.Point3d(-13.363907159494168, -6.3606993313823352, 0.0)
    vector7 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction7 = workPart.Directions.CreateDirection(origin10, vector7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin11 = NXOpen.Point3d(-13.363907159494168, -6.3606993313823352, 0.0)
    vector8 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction8 = workPart.Directions.CreateDirection(origin11, vector8, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin12 = NXOpen.Point3d(-13.363907159494168, -6.3606993313823352, 0.0)
    matrix4 = NXOpen.Matrix3x3()
    
    matrix4.Xx = 1.0
    matrix4.Xy = 0.0
    matrix4.Xz = 0.0
    matrix4.Yx = 0.0
    matrix4.Yy = 1.0
    matrix4.Yz = 0.0
    matrix4.Zx = 0.0
    matrix4.Zy = 0.0
    matrix4.Zz = 1.0
    plane4 = workPart.Planes.CreateFixedTypePlane(origin12, matrix4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform4 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane4, direction8, point11, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem4 = workPart.CoordinateSystems.CreateCoordinateSystem(xform4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point12 = NXOpen.Point3d(-13.363907159494168, -6.3606993313823352, 0.0)
    orientation4 = NXOpen.Matrix3x3()
    
    orientation4.Xx = 1.0
    orientation4.Xy = 0.0
    orientation4.Xz = 0.0
    orientation4.Yx = 0.0
    orientation4.Yy = 1.0
    orientation4.Yz = 0.0
    orientation4.Zx = 0.0
    orientation4.Zy = 0.0
    orientation4.Zz = 1.0
    addComponentBuilder7.SetInitialLocationAndOrientation(point12, orientation4)
    
    movableObjects4 = [NXOpen.NXObject.Null] * 1 
    component7 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 車三 1")
    movableObjects4[0] = component7
    componentNetwork11.SetMovingGroup(movableObjects4)
    
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork11.Solve()
    
    componentPositioner11.ClearNetwork()
    
    nErrs25 = theSession.UpdateManager.AddToDeleteList(componentNetwork11)
    
    nErrs26 = theSession.UpdateManager.DoUpdate(markId50)
    
    componentPositioner11.EndAssemblyConstraints()
    
    logicalobjects4 = addComponentBuilder7.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder7.ComponentName = "車三"
    
    nXObject5 = addComponentBuilder7.Commit()
    
    errorList4 = addComponentBuilder7.GetOperationFailures()
    
    errorList4.Dispose()
    theSession.DeleteUndoMark(markId51, None)
    
    theSession.SetUndoMarkName(markId49, "Add Component")
    
    addComponentBuilder7.Destroy()
    
    workPart.Points.DeletePoint(point10)
    
    componentPositioner11.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId50, None)
    
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder8 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner12 = workPart.ComponentAssembly.Positioner
    
    componentPositioner12.ClearNetwork()
    
    componentPositioner12.PrimaryArrangement = arrangement1
    
    componentPositioner12.BeginAssemblyConstraints()
    
    allowInterpartPositioning11 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression86 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression87 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression88 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression89 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression90 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression91 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression92 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression93 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network12 = componentPositioner12.EstablishNetwork()
    
    componentNetwork12 = network12
    componentNetwork12.MoveObjectsState = True
    
    componentNetwork12.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId53, "Add Component Dialog")
    
    componentNetwork12.MoveObjectsState = True
    
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder8.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder8.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder8.SetCount(1)
    
    addComponentBuilder8.SetScatterOption(True)
    
    addComponentBuilder8.ReferenceSet = "Unknown"
    
    addComponentBuilder8.Layer = -1
    
    # ----------------------------------------------
    #   Dialog Begin Add Component
    # ----------------------------------------------
    addComponentBuilder8.ReferenceSet = "Use Model"
    
    addComponentBuilder8.Layer = -1
    
    partstouse5 = [NXOpen.BasePart.Null] * 1 
    partstouse5[0] = part4
    addComponentBuilder8.SetPartsToAdd(partstouse5)
    
    productinterfaceobjects5 = addComponentBuilder8.GetAllProductInterfaceObjects()
    
    coordinates9 = NXOpen.Point3d(-6.4923572631145152, -8.8039623653561971, 0.0)
    point13 = workPart.Points.CreatePoint(coordinates9)
    
    coordinates10 = NXOpen.Point3d(-6.4923572631145152, -8.8039623653561971, 0.0)
    point14 = workPart.Points.CreatePoint(coordinates10)
    
    origin13 = NXOpen.Point3d(-6.4923572631145152, -8.8039623653561971, 0.0)
    vector9 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction9 = workPart.Directions.CreateDirection(origin13, vector9, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin14 = NXOpen.Point3d(-6.4923572631145152, -8.8039623653561971, 0.0)
    vector10 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction10 = workPart.Directions.CreateDirection(origin14, vector10, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin15 = NXOpen.Point3d(-6.4923572631145152, -8.8039623653561971, 0.0)
    matrix5 = NXOpen.Matrix3x3()
    
    matrix5.Xx = 1.0
    matrix5.Xy = 0.0
    matrix5.Xz = 0.0
    matrix5.Yx = 0.0
    matrix5.Yy = 1.0
    matrix5.Yz = 0.0
    matrix5.Zx = 0.0
    matrix5.Zy = 0.0
    matrix5.Zz = 1.0
    plane5 = workPart.Planes.CreateFixedTypePlane(origin15, matrix5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform5 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane5, direction10, point14, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem5 = workPart.CoordinateSystems.CreateCoordinateSystem(xform5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point15 = NXOpen.Point3d(-6.4923572631145152, -8.8039623653561971, 0.0)
    orientation5 = NXOpen.Matrix3x3()
    
    orientation5.Xx = 1.0
    orientation5.Xy = 0.0
    orientation5.Xz = 0.0
    orientation5.Yx = 0.0
    orientation5.Yy = 1.0
    orientation5.Yz = 0.0
    orientation5.Zx = 0.0
    orientation5.Zy = 0.0
    orientation5.Zz = 1.0
    addComponentBuilder8.SetInitialLocationAndOrientation(point15, orientation5)
    
    movableObjects5 = [NXOpen.NXObject.Null] * 1 
    component8 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 車三 1")
    movableObjects5[0] = component8
    componentNetwork12.SetMovingGroup(movableObjects5)
    
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork12.Solve()
    
    componentPositioner12.ClearNetwork()
    
    nErrs27 = theSession.UpdateManager.AddToDeleteList(componentNetwork12)
    
    nErrs28 = theSession.UpdateManager.DoUpdate(markId54)
    
    componentPositioner12.EndAssemblyConstraints()
    
    logicalobjects5 = addComponentBuilder8.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder8.ComponentName = "車三"
    
    nXObject6 = addComponentBuilder8.Commit()
    
    errorList5 = addComponentBuilder8.GetOperationFailures()
    
    errorList5.Dispose()
    theSession.DeleteUndoMark(markId55, None)
    
    theSession.SetUndoMarkName(markId53, "Add Component")
    
    addComponentBuilder8.Destroy()
    
    workPart.Points.DeletePoint(point13)
    
    componentPositioner12.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId54, None)
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder9 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner13 = workPart.ComponentAssembly.Positioner
    
    componentPositioner13.ClearNetwork()
    
    componentPositioner13.PrimaryArrangement = arrangement1
    
    componentPositioner13.BeginAssemblyConstraints()
    
    allowInterpartPositioning12 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression94 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression95 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression96 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression97 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression98 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression99 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression100 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression101 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network13 = componentPositioner13.EstablishNetwork()
    
    componentNetwork13 = network13
    componentNetwork13.MoveObjectsState = True
    
    componentNetwork13.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId57, "Add Component Dialog")
    
    componentNetwork13.MoveObjectsState = True
    
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder9.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder9.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder9.SetCount(1)
    
    addComponentBuilder9.SetScatterOption(True)
    
    addComponentBuilder9.ReferenceSet = "Unknown"
    
    addComponentBuilder9.Layer = -1
    
    # ----------------------------------------------
    #   Dialog Begin Add Component
    # ----------------------------------------------
    componentPositioner13.ClearNetwork()
    
    addComponentBuilder9.RemoveAddedComponents()
    
    addComponentBuilder9.Destroy()
    
    componentPositioner13.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner13.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId58, None)
    
    theSession.UndoToMark(markId57, None)
    
    theSession.DeleteUndoMark(markId57, None)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId60 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner14 = workPart.ComponentAssembly.Positioner
    
    componentPositioner14.ClearNetwork()
    
    componentPositioner14.PrimaryArrangement = arrangement1
    
    componentPositioner14.BeginAssemblyConstraints()
    
    allowInterpartPositioning13 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression102 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression103 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression104 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression105 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression106 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression107 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression108 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression109 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network14 = componentPositioner14.EstablishNetwork()
    
    componentNetwork14 = network14
    componentNetwork14.MoveObjectsState = True
    
    componentNetwork14.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork14.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId60, "Assembly Constraints Dialog")
    
    componentNetwork14.MoveObjectsState = True
    
    componentNetwork14.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId61 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    component9 = nXObject5
    face6 = component9.FindObject("PROTO#.Features|REVOLVED(1)|FACE 1")
    line7 = workPart.Lines.CreateFaceAxis(face6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line7.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    line8 = workPart.Lines.CreateFaceAxis(face2, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line8.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId62 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint5 = componentPositioner14.CreateConstraint(True)
    
    componentConstraint5 = constraint5
    componentConstraint5.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.CoAlign
    
    componentConstraint5.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    constraintReference8 = componentConstraint5.CreateConstraintReference(component9, face6, True, False, False)
    
    helpPoint7 = NXOpen.Point3d(-13.363907159494257, -8.2428641964796974, 8.8817841970012523e-16)
    constraintReference8.HelpPoint = helpPoint7
    
    constraintReference9 = componentConstraint5.CreateConstraintReference(component2, face2, True, False, False)
    
    helpPoint8 = NXOpen.Point3d(-13.261966695299936, -2.2002233422143513, 0.52369097770650752)
    constraintReference9.HelpPoint = helpPoint8
    
    constraintReference9.SetFixHint(True)
    
    objects9 = [NXOpen.TaggedObject.Null] * 1 
    objects9[0] = line7
    nErrs29 = theSession.UpdateManager.AddObjectsToDeleteList(objects9)
    
    objects10 = [NXOpen.TaggedObject.Null] * 1 
    objects10[0] = line8
    nErrs30 = theSession.UpdateManager.AddObjectsToDeleteList(objects10)
    
    componentNetwork14.Solve()
    
    component10 = nXObject6
    face7 = component10.FindObject("PROTO#.Features|REVOLVED(1)|FACE 1")
    line9 = workPart.Lines.CreateFaceAxis(face7, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line9.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    face8 = component2.FindObject("PROTO#.Features|EXTRUDE(8)|FACE 140 {(-4.2999999999998,0,0.8236909777065) EXTRUDE(2)}")
    line10 = workPart.Lines.CreateFaceAxis(face8, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line10.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId63 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint6 = componentPositioner14.CreateConstraint(True)
    
    componentConstraint6 = constraint6
    componentConstraint6.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.CoAlign
    
    componentConstraint6.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    constraintReference10 = componentConstraint6.CreateConstraintReference(component10, face7, True, False, False)
    
    helpPoint9 = NXOpen.Point3d(-6.4923572631145658, -11.999685574324005, 3.4416913763379853e-15)
    constraintReference10.HelpPoint = helpPoint9
    
    constraintReference11 = componentConstraint6.CreateConstraintReference(component2, face8, True, False, False)
    
    helpPoint10 = NXOpen.Point3d(-5.261966695299888, -1.9125441879556859, 0.5236909777065093)
    constraintReference11.HelpPoint = helpPoint10
    
    constraintReference11.SetFixHint(True)
    
    objects11 = [NXOpen.TaggedObject.Null] * 1 
    objects11[0] = line9
    nErrs31 = theSession.UpdateManager.AddObjectsToDeleteList(objects11)
    
    objects12 = [NXOpen.TaggedObject.Null] * 1 
    objects12[0] = line10
    nErrs32 = theSession.UpdateManager.AddObjectsToDeleteList(objects12)
    
    componentNetwork14.Solve()
    
    markId64 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs33 = theSession.UpdateManager.DoUpdate(markId61)
    
    componentNetwork14.Solve()
    
    componentPositioner14.ClearNetwork()
    
    nErrs34 = theSession.UpdateManager.AddToDeleteList(componentNetwork14)
    
    componentPositioner14.DeleteNonPersistentConstraints()
    
    nErrs35 = theSession.UpdateManager.DoUpdate(markId61)
    
    theSession.DeleteUndoMark(markId64, None)
    
    theSession.SetUndoMarkName(markId60, "Assembly Constraints")
    
    componentPositioner14.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner14.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId61, None)
    
    theSession.DeleteUndoMark(markId63, None)
    
    theSession.DeleteUndoMark(markId62, None)
    
    markId65 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner15 = workPart.ComponentAssembly.Positioner
    
    componentPositioner15.ClearNetwork()
    
    componentPositioner15.PrimaryArrangement = arrangement1
    
    componentPositioner15.BeginAssemblyConstraints()
    
    allowInterpartPositioning14 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression110 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression111 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression112 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression113 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression114 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression115 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression116 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression117 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network15 = componentPositioner15.EstablishNetwork()
    
    componentNetwork15 = network15
    componentNetwork15.MoveObjectsState = True
    
    componentNetwork15.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork15.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId65, "Assembly Constraints Dialog")
    
    componentNetwork15.MoveObjectsState = True
    
    componentNetwork15.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId66 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   Dialog Begin Assembly Constraints
    # ----------------------------------------------
    componentPositioner15.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner15.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId66, None)
    
    theSession.UndoToMark(markId65, None)
    
    theSession.DeleteUndoMark(markId65, None)
    
    theSession.DeleteUndoMark(markId59, None)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Components->Add Component...
    # ----------------------------------------------
    markId67 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder10 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner16 = workPart.ComponentAssembly.Positioner
    
    componentPositioner16.ClearNetwork()
    
    componentPositioner16.PrimaryArrangement = arrangement1
    
    componentPositioner16.BeginAssemblyConstraints()
    
    allowInterpartPositioning15 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression118 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression119 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression120 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression121 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression122 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression123 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression124 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression125 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network16 = componentPositioner16.EstablishNetwork()
    
    componentNetwork16 = network16
    componentNetwork16.MoveObjectsState = True
    
    componentNetwork16.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId67, "Add Component Dialog")
    
    componentNetwork16.MoveObjectsState = True
    
    markId68 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder10.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder10.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder10.SetCount(1)
    
    addComponentBuilder10.SetScatterOption(True)
    
    addComponentBuilder10.ReferenceSet = "Unknown"
    
    addComponentBuilder10.Layer = -1
    
    basePart5, partLoadStatus7 = theSession.Parts.OpenBase("C:\\Users\\Admin\\Desktop\\機器人組裝\車二.prt\\車二.prt")
    
    partLoadStatus7.Dispose()
    addComponentBuilder10.ReferenceSet = "Use Model"
    
    addComponentBuilder10.Layer = -1
    
    partstouse6 = [NXOpen.BasePart.Null] * 1 
    part5 = basePart5
    partstouse6[0] = part5
    addComponentBuilder10.SetPartsToAdd(partstouse6)
    
    productinterfaceobjects6 = addComponentBuilder10.GetAllProductInterfaceObjects()
    
    coordinates11 = NXOpen.Point3d(-18.169022667097927, -14.487835092877386, 0.0)
    point16 = workPart.Points.CreatePoint(coordinates11)
    
    coordinates12 = NXOpen.Point3d(-18.169022667097927, -14.487835092877386, 0.0)
    point17 = workPart.Points.CreatePoint(coordinates12)
    
    origin16 = NXOpen.Point3d(-18.169022667097927, -14.487835092877386, 0.0)
    vector11 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction11 = workPart.Directions.CreateDirection(origin16, vector11, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin17 = NXOpen.Point3d(-18.169022667097927, -14.487835092877386, 0.0)
    vector12 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction12 = workPart.Directions.CreateDirection(origin17, vector12, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin18 = NXOpen.Point3d(-18.169022667097927, -14.487835092877386, 0.0)
    matrix6 = NXOpen.Matrix3x3()
    
    matrix6.Xx = 1.0
    matrix6.Xy = 0.0
    matrix6.Xz = 0.0
    matrix6.Yx = 0.0
    matrix6.Yy = 1.0
    matrix6.Yz = 0.0
    matrix6.Zx = 0.0
    matrix6.Zy = 0.0
    matrix6.Zz = 1.0
    plane6 = workPart.Planes.CreateFixedTypePlane(origin18, matrix6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform6 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane6, direction12, point17, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem6 = workPart.CoordinateSystems.CreateCoordinateSystem(xform6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point18 = NXOpen.Point3d(-18.169022667097927, -14.487835092877386, 0.0)
    orientation6 = NXOpen.Matrix3x3()
    
    orientation6.Xx = 1.0
    orientation6.Xy = 0.0
    orientation6.Xz = 0.0
    orientation6.Yx = 0.0
    orientation6.Yy = 1.0
    orientation6.Yz = 0.0
    orientation6.Zx = 0.0
    orientation6.Zy = 0.0
    orientation6.Zz = 1.0
    addComponentBuilder10.SetInitialLocationAndOrientation(point18, orientation6)
    
    movableObjects6 = [NXOpen.NXObject.Null] * 1 
    component11 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 車二 1")
    movableObjects6[0] = component11
    componentNetwork16.SetMovingGroup(movableObjects6)
    
    markId69 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Rotate About Z-axis")
    
    loaded1 = componentNetwork16.IsReferencedGeometryLoaded()
    
    componentNetwork16.BeginDrag()
    
    translation2 = NXOpen.Vector3d(3.8835282466961125, -6.9510870442952628, 0.0)
    rotation1 = NXOpen.Matrix3x3()
    
    rotation1.Xx = 0.93969262078590854
    rotation1.Xy = 0.34202014332566844
    rotation1.Xz = 0.0
    rotation1.Yx = -0.34202014332566844
    rotation1.Yy = 0.93969262078590854
    rotation1.Yz = 0.0
    rotation1.Zx = 0.0
    rotation1.Zy = 0.0
    rotation1.Zz = 1.0
    componentNetwork16.DragByTransform(translation2, rotation1)
    
    translation3 = NXOpen.Vector3d(4.4580046274614133, -8.866910803299767, 0.0)
    rotation2 = NXOpen.Matrix3x3()
    
    rotation2.Xx = 0.90630778703665027
    rotation2.Xy = 0.42261826174069905
    rotation2.Xz = 0.0
    rotation2.Yx = -0.42261826174069905
    rotation2.Yy = 0.90630778703665027
    rotation2.Yz = 0.0
    rotation2.Zx = 0.0
    rotation2.Zy = 0.0
    rotation2.Zz = 1.0
    componentNetwork16.DragByTransform(translation3, rotation2)
    
    translation4 = NXOpen.Vector3d(4.8633199094690909, -10.825513190154838, 0.0)
    rotation3 = NXOpen.Matrix3x3()
    
    rotation3.Xx = 0.86602540378443904
    rotation3.Xy = 0.49999999999999956
    rotation3.Xz = 0.0
    rotation3.Yx = -0.49999999999999956
    rotation3.Yy = 0.86602540378443904
    rotation3.Yz = 0.0
    rotation3.Zx = 0.0
    rotation3.Zy = 0.0
    rotation3.Zz = 1.0
    componentNetwork16.DragByTransform(translation4, rotation3)
    
    translation5 = NXOpen.Vector3d(5.0963893986870161, -12.811988058060054, 0.0)
    rotation4 = NXOpen.Matrix3x3()
    
    rotation4.Xx = 0.81915204428899235
    rotation4.Xy = 0.5735764363510456
    rotation4.Xz = 0.0
    rotation4.Yx = -0.5735764363510456
    rotation4.Yy = 0.81915204428899235
    rotation4.Yz = 0.0
    rotation4.Zx = 0.0
    rotation4.Zy = 0.0
    rotation4.Zz = 1.0
    componentNetwork16.DragByTransform(translation5, rotation4)
    
    translation6 = NXOpen.Vector3d(4.7510105052747384, -18.787095277779478, 0.0)
    rotation5 = NXOpen.Matrix3x3()
    
    rotation5.Xx = 0.64278760968654014
    rotation5.Xy = 0.76604444311897757
    rotation5.Xz = 0.0
    rotation5.Yx = -0.76604444311897757
    rotation5.Yy = 0.64278760968654014
    rotation5.Yz = 0.0
    rotation5.Zx = 0.0
    rotation5.Zy = 0.0
    rotation5.Zz = 1.0
    componentNetwork16.DragByTransform(translation6, rotation5)
    
    translation7 = NXOpen.Vector3d(4.2906097653893767, -20.733485512633827, 0.0)
    rotation6 = NXOpen.Matrix3x3()
    
    rotation6.Xx = 0.57357643635104705
    rotation6.Xy = 0.81915204428899135
    rotation6.Xz = 0.0
    rotation6.Yx = -0.81915204428899135
    rotation6.Yy = 0.57357643635104705
    rotation6.Yz = 0.0
    rotation6.Zx = 0.0
    rotation6.Zy = 0.0
    rotation6.Zz = 1.0
    componentNetwork16.DragByTransform(translation7, rotation6)
    
    translation8 = NXOpen.Vector3d(3.662321902722546, -22.632342576566998, 0.0)
    rotation7 = NXOpen.Matrix3x3()
    
    rotation7.Xx = 0.50000000000000111
    rotation7.Xy = 0.86602540378443826
    rotation7.Xz = 0.0
    rotation7.Yx = -0.86602540378443826
    rotation7.Yy = 0.50000000000000111
    rotation7.Yz = 0.0
    rotation7.Zx = 0.0
    rotation7.Zy = 0.0
    rotation7.Zz = 1.0
    componentNetwork16.DragByTransform(translation8, rotation7)
    
    translation9 = NXOpen.Vector3d(2.8709285672797265, -24.469215020761215, 0.0)
    rotation8 = NXOpen.Matrix3x3()
    
    rotation8.Xx = 0.42261826174070066
    rotation8.Xy = 0.90630778703664971
    rotation8.Xz = 0.0
    rotation8.Yx = -0.90630778703664971
    rotation8.Yy = 0.42261826174070066
    rotation8.Yz = 0.0
    rotation8.Zx = 0.0
    rotation8.Zy = 0.0
    rotation8.Zz = 1.0
    componentNetwork16.DragByTransform(translation9, rotation8)
    
    translation10 = NXOpen.Vector3d(1.9224527401999865, -26.230123136782254, 0.0)
    rotation9 = NXOpen.Matrix3x3()
    
    rotation9.Xx = 0.34202014332567005
    rotation9.Xy = 0.93969262078590821
    rotation9.Xz = 0.0
    rotation9.Yx = -0.93969262078590821
    rotation9.Yy = 0.34202014332567005
    rotation9.Yz = 0.0
    rotation9.Zx = 0.0
    rotation9.Zy = 0.0
    rotation9.Zz = 1.0
    componentNetwork16.DragByTransform(translation10, rotation9)
    
    translation11 = NXOpen.Vector3d(-0.41573193820597254, -29.471120216667909, 0.0)
    rotation10 = NXOpen.Matrix3x3()
    
    rotation10.Xx = 0.17364817766693183
    rotation10.Xy = 0.98480775301220813
    rotation10.Xz = 0.0
    rotation10.Yx = -0.98480775301220813
    rotation10.Yy = 0.17364817766693183
    rotation10.Yz = 0.0
    rotation10.Zx = 0.0
    rotation10.Zy = 0.0
    rotation10.Zz = 1.0
    componentNetwork16.DragByTransform(translation11, rotation10)
    
    translation12 = NXOpen.Vector3d(-1.7876457922950202, -30.926543235787054, 0.0)
    rotation11 = NXOpen.Matrix3x3()
    
    rotation11.Xx = 0.087155742747659706
    rotation11.Xy = 0.99619469809174577
    rotation11.Xz = 0.0
    rotation11.Yx = -0.99619469809174577
    rotation11.Yy = 0.087155742747659706
    rotation11.Yz = 0.0
    rotation11.Zx = 0.0
    rotation11.Zy = 0.0
    rotation11.Zz = 1.0
    componentNetwork16.DragByTransform(translation12, rotation11)
    
    translation13 = NXOpen.Vector3d(-3.2811875742205068, -32.256857759975304, 0.0)
    rotation12 = NXOpen.Matrix3x3()
    
    rotation12.Xx = 1.5820678100908481e-15
    rotation12.Xy = 1.0000000000000004
    rotation12.Xz = 0.0
    rotation12.Yx = -1.0000000000000004
    rotation12.Yy = 1.5820678100908481e-15
    rotation12.Yz = 0.0
    rotation12.Zx = 0.0
    rotation12.Zy = 0.0
    rotation12.Zz = 1.0
    componentNetwork16.DragByTransform(translation13, rotation12)
    
    translation14 = NXOpen.Vector3d(-4.8849905291968021, -33.451939292437693, 0.0)
    rotation13 = NXOpen.Matrix3x3()
    
    rotation13.Xx = -0.087155742747656556
    rotation13.Xy = 0.9961946980917461
    rotation13.Xz = 0.0
    rotation13.Yx = -0.9961946980917461
    rotation13.Yy = -0.087155742747656556
    rotation13.Yz = 0.0
    rotation13.Zx = 0.0
    rotation13.Zy = 0.0
    rotation13.Zz = 1.0
    componentNetwork16.DragByTransform(translation14, rotation13)
    
    translation15 = NXOpen.Vector3d(-6.5868487483338285, -34.502692541102235, 0.0)
    rotation14 = NXOpen.Matrix3x3()
    
    rotation14.Xx = -0.17364817766692872
    rotation14.Xy = 0.9848077530122088
    rotation14.Xz = 0.0
    rotation14.Yx = -0.9848077530122088
    rotation14.Yy = -0.17364817766692872
    rotation14.Yz = 0.0
    rotation14.Zx = 0.0
    rotation14.Zy = 0.0
    rotation14.Zz = 1.0
    componentNetwork16.DragByTransform(translation15, rotation14)
    
    translation16 = NXOpen.Vector3d(-8.3738100629738685, -35.401120639284443, 0.0)
    rotation15 = NXOpen.Matrix3x3()
    
    rotation15.Xx = -0.25881904510251913
    rotation15.Xy = 0.9659258262890692
    rotation15.Xz = 0.0
    rotation15.Yx = -0.9659258262890692
    rotation15.Yy = -0.25881904510251913
    rotation15.Yz = 0.0
    rotation15.Zx = 0.0
    rotation15.Zy = 0.0
    rotation15.Zz = 1.0
    componentNetwork16.DragByTransform(translation16, rotation15)
    
    translation17 = NXOpen.Vector3d(-8.3738100629738685, -35.401120639284443, 0.0)
    rotation16 = NXOpen.Matrix3x3()
    
    rotation16.Xx = -0.25881904510251913
    rotation16.Xy = 0.9659258262890692
    rotation16.Xz = 0.0
    rotation16.Yx = -0.9659258262890692
    rotation16.Yy = -0.25881904510251913
    rotation16.Yz = 0.0
    rotation16.Zx = 0.0
    rotation16.Zy = 0.0
    rotation16.Zz = 1.0
    componentNetwork16.DragByTransform(translation17, rotation16)
    
    componentNetwork16.EndDrag()
    
    componentNetwork16.ResetDisplay()
    
    componentNetwork16.ApplyToModel()
    
    markId70 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId71 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork16.Solve()
    
    componentPositioner16.ClearNetwork()
    
    nErrs36 = theSession.UpdateManager.AddToDeleteList(componentNetwork16)
    
    nErrs37 = theSession.UpdateManager.DoUpdate(markId68)
    
    componentPositioner16.EndAssemblyConstraints()
    
    logicalobjects6 = addComponentBuilder10.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder10.ComponentName = "車二"
    
    nXObject7 = addComponentBuilder10.Commit()
    
    errorList6 = addComponentBuilder10.GetOperationFailures()
    
    errorList6.Dispose()
    theSession.DeleteUndoMark(markId70, None)
    
    theSession.SetUndoMarkName(markId67, "Add Component")
    
    addComponentBuilder10.Destroy()
    
    workPart.Points.DeletePoint(point16)
    
    componentPositioner16.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId68, None)
    
    theSession.DeleteUndoMark(markId69, None)
    
    markId72 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder11 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner17 = workPart.ComponentAssembly.Positioner
    
    componentPositioner17.ClearNetwork()
    
    componentPositioner17.PrimaryArrangement = arrangement1
    
    componentPositioner17.BeginAssemblyConstraints()
    
    allowInterpartPositioning16 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression126 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression127 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression128 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression129 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression130 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression131 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression132 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression133 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network17 = componentPositioner17.EstablishNetwork()
    
    componentNetwork17 = network17
    componentNetwork17.MoveObjectsState = True
    
    componentNetwork17.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId72, "Add Component Dialog")
    
    componentNetwork17.MoveObjectsState = True
    
    markId73 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder11.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder11.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder11.SetCount(1)
    
    addComponentBuilder11.SetScatterOption(True)
    
    addComponentBuilder11.ReferenceSet = "Unknown"
    
    addComponentBuilder11.Layer = -1
    
    # ----------------------------------------------
    #   Dialog Begin Add Component
    # ----------------------------------------------
    addComponentBuilder11.ReferenceSet = "Use Model"
    
    addComponentBuilder11.Layer = -1
    
    partstouse7 = [NXOpen.BasePart.Null] * 1 
    partstouse7[0] = part5
    addComponentBuilder11.SetPartsToAdd(partstouse7)
    
    productinterfaceobjects7 = addComponentBuilder11.GetAllProductInterfaceObjects()
    
    partstoremove1 = [NXOpen.BasePart.Null] * 1 
    partstoremove1[0] = part5
    addComponentBuilder11.RemovePartsFromSelection(partstoremove1)
    
    partstouse8 = []
    addComponentBuilder11.SetPartsToAdd(partstouse8)
    
    productinterfaceobjects8 = addComponentBuilder11.GetAllProductInterfaceObjects()
    
    addComponentBuilder11.SetCount(3)
    
    addComponentBuilder11.ReferenceSet = "Use Model"
    
    addComponentBuilder11.Layer = -1
    
    partstouse9 = [NXOpen.BasePart.Null] * 1 
    partstouse9[0] = part5
    addComponentBuilder11.SetPartsToAdd(partstouse9)
    
    productinterfaceobjects9 = addComponentBuilder11.GetAllProductInterfaceObjects()
    
    coordinates13 = NXOpen.Point3d(-22.974517240233581, -9.5419611289654469, 0.0)
    point19 = workPart.Points.CreatePoint(coordinates13)
    
    coordinates14 = NXOpen.Point3d(-22.974517240233581, -9.5419611289654469, 0.0)
    point20 = workPart.Points.CreatePoint(coordinates14)
    
    origin19 = NXOpen.Point3d(-22.974517240233581, -9.5419611289654469, 0.0)
    vector13 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction13 = workPart.Directions.CreateDirection(origin19, vector13, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin20 = NXOpen.Point3d(-22.974517240233581, -9.5419611289654469, 0.0)
    vector14 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction14 = workPart.Directions.CreateDirection(origin20, vector14, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    origin21 = NXOpen.Point3d(-22.974517240233581, -9.5419611289654469, 0.0)
    matrix7 = NXOpen.Matrix3x3()
    
    matrix7.Xx = 1.0
    matrix7.Xy = 0.0
    matrix7.Xz = 0.0
    matrix7.Yx = 0.0
    matrix7.Yy = 1.0
    matrix7.Yz = 0.0
    matrix7.Zx = 0.0
    matrix7.Zy = 0.0
    matrix7.Zz = 1.0
    plane7 = workPart.Planes.CreateFixedTypePlane(origin21, matrix7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform7 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane7, direction14, point20, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem7 = workPart.CoordinateSystems.CreateCoordinateSystem(xform7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point21 = NXOpen.Point3d(-22.974517240233581, -9.5419611289654469, 0.0)
    orientation7 = NXOpen.Matrix3x3()
    
    orientation7.Xx = 1.0
    orientation7.Xy = 0.0
    orientation7.Xz = 0.0
    orientation7.Yx = 0.0
    orientation7.Yy = 1.0
    orientation7.Yz = 0.0
    orientation7.Zx = 0.0
    orientation7.Zy = 0.0
    orientation7.Zz = 1.0
    addComponentBuilder11.SetInitialLocationAndOrientation(point21, orientation7)
    
    movableObjects7 = [NXOpen.NXObject.Null] * 3 
    component12 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 車二 1")
    movableObjects7[0] = component12
    component13 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 車二 1")
    movableObjects7[1] = component13
    component14 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 車二 1")
    movableObjects7[2] = component14
    componentNetwork17.SetMovingGroup(movableObjects7)
    
    markId74 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Rotate About Z-axis")
    
    loaded2 = componentNetwork17.IsReferencedGeometryLoaded()
    
    componentNetwork17.BeginDrag()
    
    translation18 = NXOpen.Vector3d(1.4634284549135721, -5.8083226220742068, 0.0)
    rotation17 = NXOpen.Matrix3x3()
    
    rotation17.Xx = 0.96592582628906831
    rotation17.Xy = 0.25881904510252057
    rotation17.Xz = 0.0
    rotation17.Yx = -0.25881904510252057
    rotation17.Yy = 0.96592582628906831
    rotation17.Yz = 0.0
    rotation17.Zx = 0.0
    rotation17.Zy = 0.0
    rotation17.Zz = 1.0
    componentNetwork17.DragByTransform(translation18, rotation17)
    
    translation19 = NXOpen.Vector3d(1.607992210654885, -7.8047883367890361, 0.0)
    rotation18 = NXOpen.Matrix3x3()
    
    rotation18.Xx = 0.93969262078590843
    rotation18.Xy = 0.34202014332566849
    rotation18.Xz = 0.0
    rotation18.Yx = -0.34202014332566849
    rotation18.Yy = 0.93969262078590843
    rotation18.Yz = 0.0
    rotation18.Zx = 0.0
    rotation18.Zy = 0.0
    rotation18.Zz = 1.0
    componentNetwork17.DragByTransform(translation19, rotation18)
    
    translation20 = NXOpen.Vector3d(1.5780024054244102, -9.8062564582159197, 0.0)
    rotation19 = NXOpen.Matrix3x3()
    
    rotation19.Xx = 0.90630778703665016
    rotation19.Xy = 0.42261826174069911
    rotation19.Xz = 0.0
    rotation19.Yx = -0.42261826174069911
    rotation19.Yy = 0.90630778703665016
    rotation19.Yz = 0.0
    rotation19.Zx = 0.0
    rotation19.Zy = 0.0
    rotation19.Zz = 1.0
    componentNetwork17.DragByTransform(translation20, rotation19)
    
    translation21 = NXOpen.Vector3d(1.3736872797482818, -11.797494605431307, 0.0)
    rotation20 = NXOpen.Matrix3x3()
    
    rotation20.Xx = 0.86602540378443893
    rotation20.Xy = 0.49999999999999961
    rotation20.Xz = 0.0
    rotation20.Yx = -0.49999999999999961
    rotation20.Yy = 0.86602540378443893
    rotation20.Yz = 0.0
    rotation20.Zx = 0.0
    rotation20.Zy = 0.0
    rotation20.Zz = 1.0
    componentNetwork17.DragByTransform(translation21, rotation20)
    
    translation22 = NXOpen.Vector3d(0.99660179510174984, -13.763348253792426, 0.0)
    rotation21 = NXOpen.Matrix3x3()
    
    rotation21.Xx = 0.81915204428899213
    rotation21.Xy = 0.57357643635104572
    rotation21.Xz = 0.0
    rotation21.Yx = -0.57357643635104572
    rotation21.Yy = 0.81915204428899213
    rotation21.Yz = 0.0
    rotation21.Zx = 0.0
    rotation21.Zy = 0.0
    rotation21.Zz = 1.0
    componentNetwork17.DragByTransform(translation22, rotation21)
    
    translation23 = NXOpen.Vector3d(0.44961579971341337, -15.688856070020357, 0.0)
    rotation22 = NXOpen.Matrix3x3()
    
    rotation22.Xx = 0.76604444311897846
    rotation22.Xy = 0.64278760968653892
    rotation22.Xz = 0.0
    rotation22.Yx = -0.64278760968653892
    rotation22.Yy = 0.76604444311897846
    rotation22.Yz = 0.0
    rotation22.Zx = 0.0
    rotation22.Zy = 0.0
    rotation22.Zz = 1.0
    componentNetwork17.DragByTransform(translation23, rotation22)
    
    translation24 = NXOpen.Vector3d(-1.1361447851315987, -19.360635681578554, 0.0)
    rotation23 = NXOpen.Matrix3x3()
    
    rotation23.Xx = 0.64278760968654003
    rotation23.Xy = 0.76604444311897757
    rotation23.Xz = 0.0
    rotation23.Yx = -0.76604444311897757
    rotation23.Yy = 0.64278760968654003
    rotation23.Yz = 0.0
    rotation23.Zx = 0.0
    rotation23.Zy = 0.0
    rotation23.Zz = 1.0
    componentNetwork17.DragByTransform(translation24, rotation23)
    
    translation25 = NXOpen.Vector3d(-3.3354119418498094, -22.70126827461884, 0.0)
    rotation24 = NXOpen.Matrix3x3()
    
    rotation24.Xx = 0.50000000000000089
    rotation24.Xy = 0.86602540378443826
    rotation24.Xz = 0.0
    rotation24.Yx = -0.86602540378443826
    rotation24.Yy = 0.50000000000000089
    rotation24.Yz = 0.0
    rotation24.Zx = 0.0
    rotation24.Zy = 0.0
    rotation24.Zz = 1.0
    componentNetwork17.DragByTransform(translation25, rotation24)
    
    translation26 = NXOpen.Vector3d(-7.6338526584851252, -26.872795804232108, 0.0)
    rotation25 = NXOpen.Matrix3x3()
    
    rotation25.Xx = 0.25881904510252185
    rotation25.Xy = 0.96592582628906809
    rotation25.Xz = 0.0
    rotation25.Yx = -0.96592582628906809
    rotation25.Yy = 0.25881904510252185
    rotation25.Yz = 0.0
    rotation25.Zx = 0.0
    rotation25.Zy = 0.0
    rotation25.Zz = 1.0
    componentNetwork17.DragByTransform(translation26, rotation25)
    
    translation27 = NXOpen.Vector3d(-12.865498331289052, -29.789663658452056, 0.0)
    rotation26 = NXOpen.Matrix3x3()
    
    rotation26.Xx = 1.27675647831893e-15
    rotation26.Xy = 1.0
    rotation26.Xz = 0.0
    rotation26.Yx = -1.0
    rotation26.Yy = 1.27675647831893e-15
    rotation26.Yz = 0.0
    rotation26.Zx = 0.0
    rotation26.Zy = 0.0
    rotation26.Zz = 1.0
    componentNetwork17.DragByTransform(translation27, rotation26)
    
    translation28 = NXOpen.Vector3d(-14.756520273215365, -30.446024873530355, 0.0)
    rotation27 = NXOpen.Matrix3x3()
    
    rotation27.Xx = -0.08715574274765682
    rotation27.Xy = 0.99619469809174566
    rotation27.Xz = 0.0
    rotation27.Yx = -0.99619469809174566
    rotation27.Yy = -0.08715574274765682
    rotation27.Yz = 0.0
    rotation27.Zx = 0.0
    rotation27.Zy = 0.0
    rotation27.Zz = 1.0
    componentNetwork17.DragByTransform(translation28, rotation27)
    
    translation29 = NXOpen.Vector3d(-16.697551954948423, -30.935075014123701, 0.0)
    rotation28 = NXOpen.Matrix3x3()
    
    rotation28.Xx = -0.17364817766692894
    rotation28.Xy = 0.98480775301220835
    rotation28.Xz = 0.0
    rotation28.Yx = -0.98480775301220835
    rotation28.Yy = -0.17364817766692894
    rotation28.Yz = 0.0
    rotation28.Zx = 0.0
    rotation28.Zy = 0.0
    rotation28.Zz = 1.0
    componentNetwork17.DragByTransform(translation29, rotation28)
    
    translation30 = NXOpen.Vector3d(-20.670286668078084, -31.397655869106952, 0.0)
    rotation29 = NXOpen.Matrix3x3()
    
    rotation29.Xx = -0.34202014332566727
    rotation29.Xy = 0.93969262078590898
    rotation29.Xz = 0.0
    rotation29.Yx = -0.93969262078590898
    rotation29.Yy = -0.34202014332566727
    rotation29.Yz = 0.0
    rotation29.Zx = 0.0
    rotation29.Zy = 0.0
    rotation29.Zz = 1.0
    componentNetwork17.DragByTransform(translation30, rotation29)
    
    translation31 = NXOpen.Vector3d(-18.673820953363254, -31.253092113365636, 0.0)
    rotation30 = NXOpen.Matrix3x3()
    
    rotation30.Xx = -0.2588190451025193
    rotation30.Xy = 0.96592582628906865
    rotation30.Xz = 0.0
    rotation30.Yx = -0.96592582628906865
    rotation30.Yy = -0.2588190451025193
    rotation30.Yz = 0.0
    rotation30.Zx = 0.0
    rotation30.Zy = 0.0
    rotation30.Zz = 1.0
    componentNetwork17.DragByTransform(translation31, rotation30)
    
    translation32 = NXOpen.Vector3d(-16.697551954948423, -30.935075014123701, 0.0)
    rotation31 = NXOpen.Matrix3x3()
    
    rotation31.Xx = -0.17364817766692894
    rotation31.Xy = 0.98480775301220835
    rotation31.Xz = 0.0
    rotation31.Yx = -0.98480775301220835
    rotation31.Yy = -0.17364817766692894
    rotation31.Yz = 0.0
    rotation31.Zx = 0.0
    rotation31.Zy = 0.0
    rotation31.Zz = 1.0
    componentNetwork17.DragByTransform(translation32, rotation31)
    
    translation33 = NXOpen.Vector3d(-14.756520273215365, -30.446024873530355, 0.0)
    rotation32 = NXOpen.Matrix3x3()
    
    rotation32.Xx = -0.087155742747656834
    rotation32.Xy = 0.99619469809174566
    rotation32.Xz = 0.0
    rotation32.Yx = -0.99619469809174566
    rotation32.Yy = -0.087155742747656834
    rotation32.Yz = 0.0
    rotation32.Zx = 0.0
    rotation32.Zy = 0.0
    rotation32.Zz = 1.0
    componentNetwork17.DragByTransform(translation33, rotation32)
    
    translation34 = NXOpen.Vector3d(-14.756520273215365, -30.446024873530355, 0.0)
    rotation33 = NXOpen.Matrix3x3()
    
    rotation33.Xx = -0.087155742747656834
    rotation33.Xy = 0.99619469809174566
    rotation33.Xz = 0.0
    rotation33.Yx = -0.99619469809174566
    rotation33.Yy = -0.087155742747656834
    rotation33.Yz = 0.0
    rotation33.Zx = 0.0
    rotation33.Zy = 0.0
    rotation33.Zz = 1.0
    componentNetwork17.DragByTransform(translation34, rotation33)
    
    componentNetwork17.EndDrag()
    
    componentNetwork17.ResetDisplay()
    
    componentNetwork17.ApplyToModel()
    
    markId75 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Add Component")
    
    markId76 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "AddComponent on_apply")
    
    componentNetwork17.Solve()
    
    componentPositioner17.ClearNetwork()
    
    nErrs38 = theSession.UpdateManager.AddToDeleteList(componentNetwork17)
    
    nErrs39 = theSession.UpdateManager.DoUpdate(markId73)
    
    componentPositioner17.EndAssemblyConstraints()
    
    logicalobjects7 = addComponentBuilder11.GetLogicalObjectsHavingUnassignedRequiredAttributes()
    
    addComponentBuilder11.ComponentName = "車二"
    
    nXObject8 = addComponentBuilder11.Commit()
    
    errorList7 = addComponentBuilder11.GetOperationFailures()
    
    errorList7.Dispose()
    theSession.DeleteUndoMark(markId75, None)
    
    theSession.SetUndoMarkName(markId72, "Add Component")
    
    addComponentBuilder11.Destroy()
    
    workPart.Points.DeletePoint(point19)
    
    componentPositioner17.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMark(markId73, None)
    
    theSession.DeleteUndoMark(markId74, None)
    
    markId77 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    addComponentBuilder12 = workPart.AssemblyManager.CreateAddComponentBuilder()
    
    componentPositioner18 = workPart.ComponentAssembly.Positioner
    
    componentPositioner18.ClearNetwork()
    
    componentPositioner18.PrimaryArrangement = arrangement1
    
    componentPositioner18.BeginAssemblyConstraints()
    
    allowInterpartPositioning17 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression134 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression135 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression136 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression137 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression138 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression139 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression140 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression141 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network18 = componentPositioner18.EstablishNetwork()
    
    componentNetwork18 = network18
    componentNetwork18.MoveObjectsState = True
    
    componentNetwork18.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    theSession.SetUndoMarkName(markId77, "Add Component Dialog")
    
    componentNetwork18.MoveObjectsState = True
    
    markId78 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    addComponentBuilder12.SetComponentAnchor(NXOpen.Assemblies.ProductInterface.InterfaceObject.Null)
    
    addComponentBuilder12.SetInitialLocationType(NXOpen.Assemblies.AddComponentBuilder.LocationType.Snap)
    
    addComponentBuilder12.SetCount(3)
    
    addComponentBuilder12.SetScatterOption(True)
    
    addComponentBuilder12.ReferenceSet = "Unknown"
    
    addComponentBuilder12.Layer = -1
    
    # ----------------------------------------------
    #   Dialog Begin Add Component
    # ----------------------------------------------
    componentPositioner18.ClearNetwork()
    
    addComponentBuilder12.RemoveAddedComponents()
    
    addComponentBuilder12.Destroy()
    
    componentPositioner18.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner18.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId78, None)
    
    theSession.UndoToMark(markId77, None)
    
    theSession.DeleteUndoMark(markId77, None)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId79 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId80 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner19 = workPart.ComponentAssembly.Positioner
    
    componentPositioner19.ClearNetwork()
    
    componentPositioner19.PrimaryArrangement = arrangement1
    
    componentPositioner19.BeginAssemblyConstraints()
    
    allowInterpartPositioning18 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression142 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression143 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression144 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression145 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression146 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression147 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression148 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression149 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network19 = componentPositioner19.EstablishNetwork()
    
    componentNetwork19 = network19
    componentNetwork19.MoveObjectsState = True
    
    componentNetwork19.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork19.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId80, "Assembly Constraints Dialog")
    
    componentNetwork19.MoveObjectsState = True
    
    componentNetwork19.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId81 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    component15 = nXObject7
    face9 = component15.FindObject("PROTO#.Features|BLEND(3)|FACE 1 {(0.0292893218813,0,0.7207106781187) EXTRUDE(2)}")
    line11 = workPart.Lines.CreateFaceAxis(face9, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line11.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    face10 = component15.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 140 {(0.4,0,-0.75) EXTRUDE(2)}")
    line12 = workPart.Lines.CreateFaceAxis(face10, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line12.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    face11 = component15.FindObject("PROTO#.Features|BLEND(3)|FACE 2 {(0.7707106781187,0,0.7207106781187) EXTRUDE(2)}")
    line13 = workPart.Lines.CreateFaceAxis(face11, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line13.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    objects13 = [NXOpen.TaggedObject.Null] * 1 
    objects13[0] = line13
    nErrs40 = theSession.UpdateManager.AddObjectsToDeleteList(objects13)
    
    objects14 = [NXOpen.TaggedObject.Null] * 1 
    objects14[0] = line11
    nErrs41 = theSession.UpdateManager.AddObjectsToDeleteList(objects14)
    
    line14 = workPart.Lines.CreateFaceAxis(face6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line14.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId82 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint7 = componentPositioner19.CreateConstraint(True)
    
    componentConstraint7 = constraint7
    componentConstraint7.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.CoAlign
    
    componentConstraint7.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    constraintReference12 = componentConstraint7.CreateConstraintReference(component15, face10, True, False, False)
    
    helpPoint11 = NXOpen.Point3d(-17.733143693307749, -14.353932939768656, 2.6645352591003757e-15)
    constraintReference12.HelpPoint = helpPoint11
    
    constraintReference13 = componentConstraint7.CreateConstraintReference(component9, face6, True, False, False)
    
    helpPoint12 = NXOpen.Point3d(-13.261966695299948, -17.627972915592817, 0.5236909777065123)
    constraintReference13.HelpPoint = helpPoint12
    
    constraintReference13.SetFixHint(True)
    
    objects15 = [NXOpen.TaggedObject.Null] * 1 
    objects15[0] = line12
    nErrs42 = theSession.UpdateManager.AddObjectsToDeleteList(objects15)
    
    objects16 = [NXOpen.TaggedObject.Null] * 1 
    objects16[0] = line14
    nErrs43 = theSession.UpdateManager.AddObjectsToDeleteList(objects16)
    
    componentNetwork19.Solve()
    
    face12 = component13.FindObject("PROTO#.Features|BLEND(3)|FACE 2 {(0.7707106781187,0,0.7207106781187) EXTRUDE(2)}")
    line15 = workPart.Lines.CreateFaceAxis(face12, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line15.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    face13 = component13.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 140 {(0.4,0,-0.75) EXTRUDE(2)}")
    line16 = workPart.Lines.CreateFaceAxis(face13, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line16.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    objects17 = [NXOpen.TaggedObject.Null] * 1 
    objects17[0] = line15
    nErrs44 = theSession.UpdateManager.AddObjectsToDeleteList(objects17)
    
    line17 = workPart.Lines.CreateFaceAxis(face6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line17.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId83 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint8 = componentPositioner19.CreateConstraint(True)
    
    componentConstraint8 = constraint8
    componentConstraint8.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.CoAlign
    
    componentConstraint8.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    constraintReference14 = componentConstraint8.CreateConstraintReference(component13, face13, True, False, False)
    
    helpPoint13 = NXOpen.Point3d(-22.495658437212203, -9.4230530712309708, 8.8817841970012523e-16)
    constraintReference14.HelpPoint = helpPoint13
    
    constraintReference15 = componentConstraint8.CreateConstraintReference(component9, face6, True, False, False)
    
    helpPoint14 = NXOpen.Point3d(-13.261966695299941, -8.7704048152855378, 0.52369097770650974)
    constraintReference15.HelpPoint = helpPoint14
    
    constraintReference15.SetFixHint(True)
    
    objects18 = [NXOpen.TaggedObject.Null] * 1 
    objects18[0] = line16
    nErrs45 = theSession.UpdateManager.AddObjectsToDeleteList(objects18)
    
    objects19 = [NXOpen.TaggedObject.Null] * 1 
    objects19[0] = line17
    nErrs46 = theSession.UpdateManager.AddObjectsToDeleteList(objects19)
    
    componentNetwork19.Solve()
    
    face14 = component14.FindObject("PROTO#.Features|BLEND(3)|FACE 2 {(0.7707106781187,0,0.7207106781187) EXTRUDE(2)}")
    line18 = workPart.Lines.CreateFaceAxis(face14, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line18.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    face15 = component14.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 140 {(0.4,0,-0.75) EXTRUDE(2)}")
    line19 = workPart.Lines.CreateFaceAxis(face15, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line19.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    objects20 = [NXOpen.TaggedObject.Null] * 1 
    objects20[0] = line18
    nErrs47 = theSession.UpdateManager.AddObjectsToDeleteList(objects20)
    
    line20 = workPart.Lines.CreateFaceAxis(face7, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line20.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId84 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint9 = componentPositioner19.CreateConstraint(True)
    
    componentConstraint9 = constraint9
    componentConstraint9.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.CoAlign
    
    componentConstraint9.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    constraintReference16 = componentConstraint9.CreateConstraintReference(component14, face15, True, False, False)
    
    helpPoint15 = NXOpen.Point3d(-20.232668440693864, -8.3373907543797756, 0.0)
    constraintReference16.HelpPoint = helpPoint15
    
    constraintReference17 = componentConstraint9.CreateConstraintReference(component10, face7, True, False, False)
    
    helpPoint16 = NXOpen.Point3d(-5.261966695299904, -19.978325732680659, 0.5236909777065164)
    constraintReference17.HelpPoint = helpPoint16
    
    constraintReference17.SetFixHint(True)
    
    objects21 = [NXOpen.TaggedObject.Null] * 1 
    objects21[0] = line20
    nErrs48 = theSession.UpdateManager.AddObjectsToDeleteList(objects21)
    
    objects22 = [NXOpen.TaggedObject.Null] * 1 
    objects22[0] = line19
    nErrs49 = theSession.UpdateManager.AddObjectsToDeleteList(objects22)
    
    componentNetwork19.Solve()
    
    component16 = nXObject8
    face16 = component16.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 140 {(0.4,0,-0.75) EXTRUDE(2)}")
    line21 = workPart.Lines.CreateFaceAxis(face16, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line21.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    line22 = workPart.Lines.CreateFaceAxis(face7, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line22.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId85 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint10 = componentPositioner19.CreateConstraint(True)
    
    componentConstraint10 = constraint10
    componentConstraint10.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.CoAlign
    
    componentConstraint10.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    constraintReference18 = componentConstraint10.CreateConstraintReference(component16, face16, True, False, False)
    
    helpPoint17 = NXOpen.Point3d(-22.271273630864997, -6.8583229987373882, -8.8817841970012523e-16)
    constraintReference18.HelpPoint = helpPoint17
    
    constraintReference19 = componentConstraint10.CreateConstraintReference(component10, face7, True, False, False)
    
    helpPoint18 = NXOpen.Point3d(-5.2619666952999031, -19.939099610699603, 0.5236909777065164)
    constraintReference19.HelpPoint = helpPoint18
    
    constraintReference19.SetFixHint(True)
    
    objects23 = [NXOpen.TaggedObject.Null] * 1 
    objects23[0] = line22
    nErrs50 = theSession.UpdateManager.AddObjectsToDeleteList(objects23)
    
    objects24 = [NXOpen.TaggedObject.Null] * 1 
    objects24[0] = line21
    nErrs51 = theSession.UpdateManager.AddObjectsToDeleteList(objects24)
    
    componentNetwork19.Solve()
    
    markId86 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs52 = theSession.UpdateManager.DoUpdate(markId81)
    
    componentNetwork19.Solve()
    
    componentPositioner19.ClearNetwork()
    
    nErrs53 = theSession.UpdateManager.AddToDeleteList(componentNetwork19)
    
    componentPositioner19.DeleteNonPersistentConstraints()
    
    nErrs54 = theSession.UpdateManager.DoUpdate(markId81)
    
    theSession.DeleteUndoMark(markId86, None)
    
    theSession.SetUndoMarkName(markId80, "Assembly Constraints")
    
    componentPositioner19.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner19.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId81, None)
    
    theSession.DeleteUndoMark(markId85, None)
    
    theSession.DeleteUndoMark(markId84, None)
    
    theSession.DeleteUndoMark(markId83, None)
    
    theSession.DeleteUndoMark(markId82, None)
    
    markId87 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner20 = workPart.ComponentAssembly.Positioner
    
    componentPositioner20.ClearNetwork()
    
    componentPositioner20.PrimaryArrangement = arrangement1
    
    componentPositioner20.BeginAssemblyConstraints()
    
    allowInterpartPositioning19 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression150 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression151 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression152 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression153 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression154 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression155 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression156 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression157 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network20 = componentPositioner20.EstablishNetwork()
    
    componentNetwork20 = network20
    componentNetwork20.MoveObjectsState = True
    
    componentNetwork20.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork20.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId87, "Assembly Constraints Dialog")
    
    componentNetwork20.MoveObjectsState = True
    
    componentNetwork20.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId88 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   Dialog Begin Assembly Constraints
    # ----------------------------------------------
    line23 = workPart.Lines.CreateFaceAxis(face7, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line23.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    face17 = component14.FindObject("PROTO#.Features|BLEND(3)|FACE 1 {(0.0292893218813,0,0.7207106781187) EXTRUDE(2)}")
    line24 = workPart.Lines.CreateFaceAxis(face17, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line24.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    objects25 = [NXOpen.TaggedObject.Null] * 1 
    objects25[0] = line23
    nErrs55 = theSession.UpdateManager.AddObjectsToDeleteList(objects25)
    
    objects26 = [NXOpen.TaggedObject.Null] * 1 
    objects26[0] = line24
    nErrs56 = theSession.UpdateManager.AddObjectsToDeleteList(objects26)
    
    scaleAboutPoint47 = NXOpen.Point3d(-12.964122653254831, -5.2066861771692992, 0.0)
    viewCenter47 = NXOpen.Point3d(12.964122653254845, 5.2066861771692743, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint47, viewCenter47)
    
    scaleAboutPoint48 = NXOpen.Point3d(-10.371298122603864, -4.1653489417354415, 0.0)
    viewCenter48 = NXOpen.Point3d(10.371298122603879, 4.1653489417354157, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint48, viewCenter48)
    
    face18 = component10.FindObject("PROTO#.Features|BLEND(2)|FACE 2 {(0,-11.9707106781187,-0.2707106781187) REVOLVED(1)}")
    line25 = workPart.Lines.CreateFaceAxis(face18, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line25.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint49 = NXOpen.Point3d(-8.2970384980830882, -3.2817900753067133, 0.0)
    viewCenter49 = NXOpen.Point3d(8.2970384980831025, 3.2817900753066893, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint49, viewCenter49)
    
    line26 = workPart.Lines.CreateFaceAxis(face7, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line26.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId89 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint11 = componentPositioner20.CreateConstraint(True)
    
    componentConstraint11 = constraint11
    componentConstraint11.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.CoAlign
    
    componentConstraint11.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    face19 = component14.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 120 {(0,0,0) EXTRUDE(2)}")
    constraintReference20 = componentConstraint11.CreateConstraintReference(component14, face19, False, False, False)
    
    helpPoint19 = NXOpen.Point3d(-4.9374052563982644, -9.7546781525459316, 0.21149981589559325)
    constraintReference20.HelpPoint = helpPoint19
    
    face20 = component10.FindObject("PROTO#.Features|REVOLVED(1)|FACE 3")
    constraintReference21 = componentConstraint11.CreateConstraintReference(component10, face20, False, False, False)
    
    helpPoint20 = NXOpen.Point3d(-5.3918029293092715, -20.803962365299807, 0.52055749288200648)
    constraintReference21.HelpPoint = helpPoint20
    
    constraintReference21.SetFixHint(True)
    
    objects27 = [NXOpen.TaggedObject.Null] * 1 
    objects27[0] = line26
    nErrs57 = theSession.UpdateManager.AddObjectsToDeleteList(objects27)
    
    objects28 = [NXOpen.TaggedObject.Null] * 1 
    objects28[0] = line25
    nErrs58 = theSession.UpdateManager.AddObjectsToDeleteList(objects28)
    
    componentNetwork20.Solve()
    
    line27 = workPart.Lines.CreateFaceAxis(face6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line27.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    objects29 = [NXOpen.TaggedObject.Null] * 1 
    objects29[0] = line27
    nErrs59 = theSession.UpdateManager.AddObjectsToDeleteList(objects29)
    
    markId90 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint12 = componentPositioner20.CreateConstraint(True)
    
    componentConstraint12 = constraint12
    componentConstraint12.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.CoAlign
    
    componentConstraint12.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    face21 = component15.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 120 {(0,0,0) EXTRUDE(2)}")
    constraintReference22 = componentConstraint12.CreateConstraintReference(component15, face21, False, False, False)
    
    helpPoint21 = NXOpen.Point3d(-12.798082485378695, -15.674205423393015, 0.45151083017998345)
    constraintReference22.HelpPoint = helpPoint21
    
    face22 = component9.FindObject("PROTO#.Features|REVOLVED(1)|FACE 3")
    constraintReference23 = componentConstraint12.CreateConstraintReference(component9, face22, False, False, False)
    
    helpPoint22 = NXOpen.Point3d(-13.307787327367114, -18.36069933121226, 0.57168053567664867)
    constraintReference23.HelpPoint = helpPoint22
    
    constraintReference23.SetFixHint(True)
    
    componentNetwork20.Solve()
    
    line28 = workPart.Lines.CreateFaceAxis(face6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line28.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = -0.26641558747904875
    rotMatrix2.Xy = 0.86189627673781988
    rotMatrix2.Xz = -0.43145978131649942
    rotMatrix2.Yx = -0.80318808540917241
    rotMatrix2.Yy = 0.048939733706665024
    rotMatrix2.Yz = 0.59371188460521196
    rotMatrix2.Zx = 0.5328335895989923
    rotMatrix2.Zy = 0.50471745621705
    rotMatrix2.Zz = 0.67922651242781085
    translation35 = NXOpen.Point3d(8.9702443705341501, -2.7487617297267324, 6.0282129955109083)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation35, 19.651527373813771)
    
    scaleAboutPoint50 = NXOpen.Point3d(-2.5446495353147238, 1.5887229903023086, 0.0)
    viewCenter50 = NXOpen.Point3d(2.5446495353147434, -1.588722990302335, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint50, viewCenter50)
    
    scaleAboutPoint51 = NXOpen.Point3d(-1.0555583257601755, 1.8526125717423527, 0.0)
    viewCenter51 = NXOpen.Point3d(1.0555583257601995, -1.8526125717423803, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint51, viewCenter51)
    
    scaleAboutPoint52 = NXOpen.Point3d(-0.78412904199327094, 1.4993236627124134, 0.0)
    viewCenter52 = NXOpen.Point3d(0.78412904199329148, -1.4993236627124413, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint52, viewCenter52)
    
    scaleAboutPoint53 = NXOpen.Point3d(-0.44807373828186287, 1.2477130250618222, 0.0)
    viewCenter53 = NXOpen.Point3d(0.44807373828188757, -1.2477130250618504, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint53, viewCenter53)
    
    scaleAboutPoint54 = NXOpen.Point3d(-0.42222333030406212, 1.5596412813272813, 0.0)
    viewCenter54 = NXOpen.Point3d(0.42222333030408637, -1.5596412813273093, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint54, viewCenter54)
    
    scaleAboutPoint55 = NXOpen.Point3d(-0.47392414625966489, 1.9495516016591046, 0.0)
    viewCenter55 = NXOpen.Point3d(0.47392414625968693, -1.949551601659133, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint55, viewCenter55)
    
    scaleAboutPoint56 = NXOpen.Point3d(-0.37698511634291365, 2.4773307645391967, 0.0)
    viewCenter56 = NXOpen.Point3d(0.37698511634293319, -2.4773307645392277, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint56, viewCenter56)
    
    scaleAboutPoint57 = NXOpen.Point3d(0.033659385387769164, 3.1808119191434003, 0.0)
    viewCenter57 = NXOpen.Point3d(-0.033659385387750505, -3.1808119191434332, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint57, viewCenter57)
    
    scaleAboutPoint58 = NXOpen.Point3d(0.48385366494907323, 3.9970520147966071, 0.0)
    viewCenter58 = NXOpen.Point3d(-0.48385366494905169, -3.9970520147966391, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint58, viewCenter58)
    
    scaleAboutPoint59 = NXOpen.Point3d(3.7603844612889357, 4.3914979373094312, 0.0)
    viewCenter59 = NXOpen.Point3d(-3.7603844612889152, -4.3914979373094623, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint59, viewCenter59)
    
    face23 = component16.FindObject("PROTO#.Features|BLEND(3)|FACE 2 {(0.7707106781187,0,0.7207106781187) EXTRUDE(2)}")
    line29 = workPart.Lines.CreateFaceAxis(face23, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line29.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint60 = NXOpen.Point3d(3.1345302642352544, 3.5131983498475434, 0.0)
    viewCenter60 = NXOpen.Point3d(-3.1345302642352331, -3.5131983498475723, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint60, viewCenter60)
    
    scaleAboutPoint61 = NXOpen.Point3d(2.5244539040820895, 2.7937289871841555, 0.0)
    viewCenter61 = NXOpen.Point3d(-2.5244539040820664, -2.7937289871841813, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint61, viewCenter61)
    
    scaleAboutPoint62 = NXOpen.Point3d(2.0195631232656734, 2.154200664816694, 0.0)
    viewCenter62 = NXOpen.Point3d(-2.0195631232656508, -2.1542006648167193, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint62, viewCenter62)
    
    scaleAboutPoint63 = NXOpen.Point3d(1.3463754155104535, 1.4971694620475997, 0.0)
    viewCenter63 = NXOpen.Point3d(-1.3463754155104295, -1.4971694620476244, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint63, viewCenter63)
    
    line30 = workPart.Lines.CreateFaceAxis(face16, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line30.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    face24 = component16.FindObject("PROTO#.Features|BLEND(3)|FACE 1 {(0.0292893218813,0,0.7207106781187) EXTRUDE(2)}")
    line31 = workPart.Lines.CreateFaceAxis(face24, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line31.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    objects30 = [NXOpen.TaggedObject.Null] * 1 
    objects30[0] = line30
    nErrs60 = theSession.UpdateManager.AddObjectsToDeleteList(objects30)
    
    objects31 = [NXOpen.TaggedObject.Null] * 1 
    objects31[0] = line31
    nErrs61 = theSession.UpdateManager.AddObjectsToDeleteList(objects31)
    
    objects32 = [NXOpen.TaggedObject.Null] * 1 
    objects32[0] = line28
    nErrs62 = theSession.UpdateManager.AddObjectsToDeleteList(objects32)
    
    objects33 = [NXOpen.TaggedObject.Null] * 1 
    objects33[0] = line29
    nErrs63 = theSession.UpdateManager.AddObjectsToDeleteList(objects33)
    
    markId91 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint13 = componentPositioner20.CreateConstraint(True)
    
    componentConstraint13 = constraint13
    componentConstraint13.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.CoAlign
    
    componentConstraint13.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    face25 = component10.FindObject("PROTO#.Features|REVOLVED(1)|FACE 2")
    constraintReference24 = componentConstraint13.CreateConstraintReference(component10, face25, False, False, False)
    
    helpPoint23 = NXOpen.Point3d(-5.3409915615950396, -8.8039623654698822, 0.591570881033193)
    constraintReference24.HelpPoint = helpPoint23
    
    face26 = component16.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 130 {(0.8,0,0) EXTRUDE(2)}")
    constraintReference25 = componentConstraint13.CreateConstraintReference(component16, face26, False, False, False)
    
    helpPoint24 = NXOpen.Point3d(-5.5286147108538337, -7.5242516565748421, 0.82731406459942181)
    constraintReference25.HelpPoint = helpPoint24
    
    constraintReference25.SetFixHint(True)
    
    componentNetwork20.Solve()
    
    scaleAboutPoint64 = NXOpen.Point3d(1.6199588999421752, 1.5596412813272829, 0.0)
    viewCenter64 = NXOpen.Point3d(-1.619958899942151, -1.5596412813273095, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint64, viewCenter64)
    
    scaleAboutPoint65 = NXOpen.Point3d(2.0249486249277142, 1.9495516016591063, 0.0)
    viewCenter65 = NXOpen.Point3d(-2.024948624927692, -1.949551601659133, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint65, viewCenter65)
    
    scaleAboutPoint66 = NXOpen.Point3d(2.5311857811596403, 2.4369395020738862, 0.0)
    viewCenter66 = NXOpen.Point3d(-2.531185781159615, -2.4369395020739124, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint66, viewCenter66)
    
    scaleAboutPoint67 = NXOpen.Point3d(3.1639822264495479, 3.0461743775923624, 0.0)
    viewCenter67 = NXOpen.Point3d(-3.1639822264495221, -3.0461743775923869, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint67, viewCenter67)
    
    scaleAboutPoint68 = NXOpen.Point3d(3.9970520147966355, 4.3967572162762725, 0.0)
    viewCenter68 = NXOpen.Point3d(-3.9970520147966071, -4.3967572162762973, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint68, viewCenter68)
    
    scaleAboutPoint69 = NXOpen.Point3d(4.9963150184957881, 5.4959465203453428, 0.0)
    viewCenter69 = NXOpen.Point3d(-4.9963150184957676, -5.4959465203453677, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint69, viewCenter69)
    
    scaleAboutPoint70 = NXOpen.Point3d(6.2453937731197326, 6.9028036439744165, 0.0)
    viewCenter70 = NXOpen.Point3d(-6.2453937731197104, -6.9028036439744422, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint70, viewCenter70)
    
    scaleAboutPoint71 = NXOpen.Point3d(7.8067422163996563, 8.9572094903953765, 0.0)
    viewCenter71 = NXOpen.Point3d(-7.8067422163996358, -8.9572094903954014, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint71, viewCenter71)
    
    scaleAboutPoint72 = NXOpen.Point3d(11.24787200915477, 14.58628150958881, 0.0)
    viewCenter72 = NXOpen.Point3d(-11.247872009154753, -14.586281509588833, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint72, viewCenter72)
    
    scaleAboutPoint73 = NXOpen.Point3d(9.1215619581090746, 12.16208261081208, 0.0)
    viewCenter73 = NXOpen.Point3d(-9.1215619581090603, -12.162082610812099, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint73, viewCenter73)
    
    scaleAboutPoint74 = NXOpen.Point3d(7.0671561116881083, 9.9926300369915477, 0.0)
    viewCenter74 = NXOpen.Point3d(-7.0671561116880977, -9.9926300369915655, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint74, viewCenter74)
    
    scaleAboutPoint75 = NXOpen.Point3d(5.4433537306769875, 8.4411427417744367, 0.0)
    viewCenter75 = NXOpen.Point3d(-5.4433537306769741, -8.4411427417744544, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint75, viewCenter75)
    
    scaleAboutPoint76 = NXOpen.Point3d(4.2915716369395351, 7.0263966996951108, 0.0)
    viewCenter76 = NXOpen.Point3d(-4.291571636939528, -7.0263966996951233, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint76, viewCenter76)
    
    line32 = workPart.Lines.CreateFaceAxis(face6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line32.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint77 = NXOpen.Point3d(3.4500870022455103, 5.6716064378377276, 0.0)
    viewCenter77 = NXOpen.Point3d(-3.4500870022454992, -5.6716064378377418, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint77, viewCenter77)
    
    scaleAboutPoint78 = NXOpen.Point3d(2.8139246184168263, 4.5642126585803862, 0.0)
    viewCenter78 = NXOpen.Point3d(-2.8139246184168161, -4.5642126585804048, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint78, viewCenter78)
    
    scaleAboutPoint79 = NXOpen.Point3d(3.5174057730210304, 5.7052658232254849, 0.0)
    viewCenter79 = NXOpen.Point3d(-3.5174057730210215, -5.7052658232255036, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint79, viewCenter79)
    
    scaleAboutPoint80 = NXOpen.Point3d(4.3967572162762858, 7.1315822790318579, 0.0)
    viewCenter80 = NXOpen.Point3d(-4.3967572162762787, -7.1315822790318792, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint80, viewCenter80)
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = -0.13399663219446684
    rotMatrix3.Xy = 0.95623977493113477
    rotMatrix3.Xz = -0.26009689617563425
    rotMatrix3.Yx = -0.80983866077313138
    rotMatrix3.Yy = 0.045604813785243593
    rotMatrix3.Yz = 0.58487737558978825
    rotMatrix3.Zx = 0.57114468051250189
    rotMatrix3.Zy = 0.28900812064589382
    rotMatrix3.Zz = 0.76828904724914848
    translation36 = NXOpen.Point3d(10.775605553662693, -1.5887541386988353, 4.3726864206470264)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation36, 10.061582015392661)
    
    scaleAboutPoint81 = NXOpen.Point3d(6.1533563912000684, 9.624480509312912, 0.0)
    viewCenter81 = NXOpen.Point3d(-6.1533563912000595, -9.6244805093129315, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint81, viewCenter81)
    
    scaleAboutPoint82 = NXOpen.Point3d(7.6916954890000797, 12.030600636641143, 0.0)
    viewCenter82 = NXOpen.Point3d(-7.6916954890000797, -12.030600636641159, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint82, viewCenter82)
    
    scaleAboutPoint83 = NXOpen.Point3d(9.6146193612500994, 15.038250795801428, 0.0)
    viewCenter83 = NXOpen.Point3d(-9.614619361250103, -15.038250795801448, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint83, viewCenter83)
    
    scaleAboutPoint84 = NXOpen.Point3d(7.691695489000077, 12.030600636641138, 0.0)
    viewCenter84 = NXOpen.Point3d(-7.691695489000077, -12.030600636641154, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint84, viewCenter84)
    
    scaleAboutPoint85 = NXOpen.Point3d(6.1533563912000648, 9.6244805093129102, 0.0)
    viewCenter85 = NXOpen.Point3d(-6.1533563912000648, -9.6244805093129298, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint85, viewCenter85)
    
    scaleAboutPoint86 = NXOpen.Point3d(4.9226851129600542, 7.6995844074503248, 0.0)
    viewCenter86 = NXOpen.Point3d(-4.9226851129600471, -7.699584407450347, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint86, viewCenter86)
    
    scaleAboutPoint87 = NXOpen.Point3d(3.938148090368045, 6.1596675259602556, 0.0)
    viewCenter87 = NXOpen.Point3d(-3.9381480903680379, -6.1596675259602813, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint87, viewCenter87)
    
    scaleAboutPoint88 = NXOpen.Point3d(3.1505184722944364, 4.9411977749233085, 0.0)
    viewCenter88 = NXOpen.Point3d(-3.1505184722944297, -4.9411977749233307, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint88, viewCenter88)
    
    scaleAboutPoint89 = NXOpen.Point3d(2.5634987911318836, 3.9314162132904791, 0.0)
    viewCenter89 = NXOpen.Point3d(-2.5634987911318765, -3.9314162132905004, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint89, viewCenter89)
    
    scaleAboutPoint90 = NXOpen.Point3d(2.068032638224043, 3.1365161679731139, 0.0)
    viewCenter90 = NXOpen.Point3d(-2.0680326382240355, -3.1365161679731353, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint90, viewCenter90)
    
    objects34 = [NXOpen.TaggedObject.Null] * 1 
    objects34[0] = line32
    nErrs64 = theSession.UpdateManager.AddObjectsToDeleteList(objects34)
    
    markId92 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint14 = componentPositioner20.CreateConstraint(True)
    
    componentConstraint14 = constraint14
    componentConstraint14.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.CoAlign
    
    componentConstraint14.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    face27 = component9.FindObject("PROTO#.Features|REVOLVED(1)|FACE 2")
    constraintReference26 = componentConstraint14.CreateConstraintReference(component9, face27, False, False, False)
    
    helpPoint25 = NXOpen.Point3d(-13.377096410554477, -6.3606993313823343, 0.51594184251342778)
    constraintReference26.HelpPoint = helpPoint25
    
    face28 = component13.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 130 {(0.8,0,0) EXTRUDE(2)}")
    constraintReference27 = componentConstraint14.CreateConstraintReference(component13, face28, False, False, False)
    
    helpPoint26 = NXOpen.Point3d(-13.727293604947807, -10.008634209552959, 0.56299862703753023)
    constraintReference27.HelpPoint = helpPoint26
    
    constraintReference27.SetFixHint(True)
    
    componentNetwork20.Solve()
    
    markId93 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs65 = theSession.UpdateManager.DoUpdate(markId88)
    
    componentNetwork20.Solve()
    
    componentPositioner20.ClearNetwork()
    
    nErrs66 = theSession.UpdateManager.AddToDeleteList(componentNetwork20)
    
    componentPositioner20.DeleteNonPersistentConstraints()
    
    nErrs67 = theSession.UpdateManager.DoUpdate(markId88)
    
    theSession.DeleteUndoMark(markId93, None)
    
    theSession.SetUndoMarkName(markId87, "Assembly Constraints")
    
    componentPositioner20.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner20.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId88, None)
    
    theSession.DeleteUndoMark(markId92, None)
    
    theSession.DeleteUndoMark(markId91, None)
    
    theSession.DeleteUndoMark(markId90, None)
    
    theSession.DeleteUndoMark(markId89, None)
    
    markId94 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner21 = workPart.ComponentAssembly.Positioner
    
    componentPositioner21.ClearNetwork()
    
    componentPositioner21.PrimaryArrangement = arrangement1
    
    componentPositioner21.BeginAssemblyConstraints()
    
    allowInterpartPositioning20 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression158 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression159 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression160 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression161 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression162 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression163 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression164 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression165 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network21 = componentPositioner21.EstablishNetwork()
    
    componentNetwork21 = network21
    componentNetwork21.MoveObjectsState = True
    
    componentNetwork21.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork21.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId94, "Assembly Constraints Dialog")
    
    componentNetwork21.MoveObjectsState = True
    
    componentNetwork21.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId95 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   Dialog Begin Assembly Constraints
    # ----------------------------------------------
    scaleAboutPoint91 = NXOpen.Point3d(-0.2068032638224003, 0.24127047445946068, 0.0)
    viewCenter91 = NXOpen.Point3d(0.20680326382240738, -0.24127047445948183, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint91, viewCenter91)
    
    scaleAboutPoint92 = NXOpen.Point3d(-0.16544261105792069, 0.19301637956756659, 0.0)
    viewCenter92 = NXOpen.Point3d(0.16544261105792726, -0.1930163795675873, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint92, viewCenter92)
    
    scaleAboutPoint93 = NXOpen.Point3d(-0.13235408884633579, 0.15441310365405103, 0.0)
    viewCenter93 = NXOpen.Point3d(0.13235408884634106, -0.1544131036540721, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint93, viewCenter93)
    
    scaleAboutPoint94 = NXOpen.Point3d(-0.16544261105792163, 0.19301637956756612, 0.0)
    viewCenter94 = NXOpen.Point3d(0.16544261105792443, -0.19301637956758777, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint94, viewCenter94)
    
    scaleAboutPoint95 = NXOpen.Point3d(-0.20680326382240199, 0.24127047445946118, 0.0)
    viewCenter95 = NXOpen.Point3d(0.20680326382240555, -0.24127047445948116, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint95, viewCenter95)
    
    scaleAboutPoint96 = NXOpen.Point3d(-0.25850407977800327, 0.30158809307432866, 0.0)
    viewCenter96 = NXOpen.Point3d(0.25850407977800616, -0.30158809307434997, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint96, viewCenter96)
    
    scaleAboutPoint97 = NXOpen.Point3d(-0.32313009972250223, 0.37698511634291265, 0.0)
    viewCenter97 = NXOpen.Point3d(0.32313009972250956, -0.37698511634293469, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint97, viewCenter97)
    
    scaleAboutPoint98 = NXOpen.Point3d(-0.40391262465313121, 0.47123139542864428, 0.0)
    viewCenter98 = NXOpen.Point3d(0.40391262465313349, -0.47123139542866493, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint98, viewCenter98)
    
    scaleAboutPoint99 = NXOpen.Point3d(-0.50489078081641392, 0.58903924428580678, 0.0)
    viewCenter99 = NXOpen.Point3d(0.50489078081641681, -0.58903924428582966, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint99, viewCenter99)
    
    scaleAboutPoint100 = NXOpen.Point3d(-0.63111347602051593, 0.73629905535726226, 0.0)
    viewCenter100 = NXOpen.Point3d(0.63111347602051948, -0.73629905535728202, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint100, viewCenter100)
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = 0.29414500144944444
    rotMatrix4.Xy = 0.91204386252608161
    rotMatrix4.Xz = 0.28575288441382141
    rotMatrix4.Yx = -0.8101218505686858
    rotMatrix4.Yy = 0.079279288712613513
    rotMatrix4.Yz = 0.58087639099243371
    rotMatrix4.Zx = 0.50713046186704436
    rotMatrix4.Zy = -0.40235654239708174
    rotMatrix4.Zz = 0.76218626820272062
    translation37 = NXOpen.Point3d(6.6134920489732778, -7.7195030434294667, -1.7766803544444114)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation37, 10.061582015392663)
    
    line33 = workPart.Lines.CreateFaceAxis(face13, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line33.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    face29 = component13.FindObject("PROTO#.Features|BLEND(3)|FACE 1 {(0.0292893218813,0,0.7207106781187) EXTRUDE(2)}")
    line34 = workPart.Lines.CreateFaceAxis(face29, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line34.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    line35 = workPart.Lines.CreateFaceAxis(face6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line35.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    objects35 = [NXOpen.TaggedObject.Null] * 1 
    objects35[0] = line35
    nErrs68 = theSession.UpdateManager.AddObjectsToDeleteList(objects35)
    
    objects36 = [NXOpen.TaggedObject.Null] * 1 
    objects36[0] = line33
    nErrs69 = theSession.UpdateManager.AddObjectsToDeleteList(objects36)
    
    objects37 = [NXOpen.TaggedObject.Null] * 1 
    objects37[0] = line34
    nErrs70 = theSession.UpdateManager.AddObjectsToDeleteList(objects37)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = -0.043929007502497563
    rotMatrix5.Xy = 0.97982021699666044
    rotMatrix5.Xz = -0.19499380673362313
    rotMatrix5.Yx = -0.81681993415618737
    rotMatrix5.Yy = 0.077154788770090021
    rotMatrix5.Yz = 0.57171000842641317
    rotMatrix5.Zx = 0.57521773048553992
    rotMatrix5.Zy = 0.18438948162643845
    rotMatrix5.Zz = 0.79694735183737508
    translation38 = NXOpen.Point3d(6.2613882660765796, -7.7562498813586886, 3.4493023329850576)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation38, 10.061582015392663)
    
    componentPositioner21.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner21.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId95, None)
    
    theSession.UndoToMark(markId94, None)
    
    theSession.DeleteUndoMark(markId94, None)
    
    theSession.DeleteUndoMark(markId79, None)
    
    # ----------------------------------------------
    #   Menu: Assemblies->Component Position->Assembly Constraints...
    # ----------------------------------------------
    markId96 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId97 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner22 = workPart.ComponentAssembly.Positioner
    
    componentPositioner22.ClearNetwork()
    
    componentPositioner22.PrimaryArrangement = arrangement1
    
    componentPositioner22.BeginAssemblyConstraints()
    
    allowInterpartPositioning21 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression166 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression167 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression168 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression169 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression170 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression171 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression172 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression173 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network22 = componentPositioner22.EstablishNetwork()
    
    componentNetwork22 = network22
    componentNetwork22.MoveObjectsState = True
    
    componentNetwork22.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork22.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId97, "Assembly Constraints Dialog")
    
    componentNetwork22.MoveObjectsState = True
    
    componentNetwork22.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId98 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    line36 = workPart.Lines.CreateFaceAxis(face12, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line36.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    line37 = workPart.Lines.CreateFaceAxis(face13, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line37.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    objects38 = [NXOpen.TaggedObject.Null] * 1 
    objects38[0] = line36
    nErrs71 = theSession.UpdateManager.AddObjectsToDeleteList(objects38)
    
    objects39 = [NXOpen.TaggedObject.Null] * 1 
    objects39[0] = line37
    nErrs72 = theSession.UpdateManager.AddObjectsToDeleteList(objects39)
    
    line38 = workPart.Lines.CreateFaceAxis(face12, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line38.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint101 = NXOpen.Point3d(-3.1029745904342083, 2.5244539040820619, 0.0)
    viewCenter101 = NXOpen.Point3d(3.1029745904342172, -2.5244539040820775, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint101, viewCenter101)
    
    face30 = component9.FindObject("PROTO#.Features|BLEND(2)|FACE 1 {(0,-0.0292893218813,0.2707106781187) REVOLVED(1)}")
    line39 = workPart.Lines.CreateFaceAxis(face30, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line39.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint102 = NXOpen.Point3d(-2.3351198612759125, 1.7040063852553908, 0.0)
    viewCenter102 = NXOpen.Point3d(2.3351198612759196, -1.704006385255407, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint102, viewCenter102)
    
    scaleAboutPoint103 = NXOpen.Point3d(-1.8680958890207284, 1.3463754155104282, 0.0)
    viewCenter103 = NXOpen.Point3d(1.8680958890207355, -1.3463754155104468, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint103, viewCenter103)
    
    scaleAboutPoint104 = NXOpen.Point3d(-1.4944767112165818, 1.0771003324083392, 0.0)
    viewCenter104 = NXOpen.Point3d(1.4944767112165864, -1.077100332408361, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint104, viewCenter104)
    
    scaleAboutPoint105 = NXOpen.Point3d(-1.1955813689732675, 0.86168026592666969, 0.0)
    viewCenter105 = NXOpen.Point3d(1.1955813689732693, -0.86168026592669167, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint105, viewCenter105)
    
    objects40 = [NXOpen.TaggedObject.Null] * 1 
    objects40[0] = line38
    nErrs73 = theSession.UpdateManager.AddObjectsToDeleteList(objects40)
    
    objects41 = [NXOpen.TaggedObject.Null] * 1 
    objects41[0] = line39
    nErrs74 = theSession.UpdateManager.AddObjectsToDeleteList(objects41)
    
    scaleAboutPoint106 = NXOpen.Point3d(-0.21542006648166812, 0.52562496221526489, 0.0)
    viewCenter106 = NXOpen.Point3d(0.21542006648167178, -0.52562496221528621, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint106, viewCenter106)
    
    scaleAboutPoint107 = NXOpen.Point3d(-0.26927508310208609, 0.657031202769083, 0.0)
    viewCenter107 = NXOpen.Point3d(0.26927508310208975, -0.65703120276910509, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint107, viewCenter107)
    
    scaleAboutPoint108 = NXOpen.Point3d(-0.33659385387760871, 0.82128900346135725, 0.0)
    viewCenter108 = NXOpen.Point3d(0.33659385387761104, -0.8212890034613779, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint108, viewCenter108)
    
    scaleAboutPoint109 = NXOpen.Point3d(-0.42074231734701079, 1.0266112543266976, 0.0)
    viewCenter109 = NXOpen.Point3d(0.42074231734701939, -1.0266112543267205, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint109, viewCenter109)
    
    scaleAboutPoint110 = NXOpen.Point3d(-0.52592789668376161, 1.2832640679083755, 0.0)
    viewCenter110 = NXOpen.Point3d(0.52592789668376883, -1.2832640679083971, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint110, viewCenter110)
    
    scaleAboutPoint111 = NXOpen.Point3d(-0.65740987085470426, 1.6040800848854693, 0.0)
    viewCenter111 = NXOpen.Point3d(0.6574098708547087, -1.6040800848854939, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint111, viewCenter111)
    
    markId99 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint15 = componentPositioner22.CreateConstraint(True)
    
    componentConstraint15 = constraint15
    componentConstraint15.ConstraintType = NXOpen.Positioning.Constraint.Type.Distance
    
    constraintReference28 = componentConstraint15.CreateConstraintReference(component13, face28, False, False, False)
    
    helpPoint27 = NXOpen.Point3d(-12.763662028906072, -10.008634209552959, 0.47063620227134972)
    constraintReference28.HelpPoint = helpPoint27
    
    face31 = component2.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 120 {(-7.5,4,2.8769308262358) EXTRUDE(2)}")
    constraintReference29 = componentConstraint15.CreateConstraintReference(component2, face31, False, False, False)
    
    helpPoint28 = NXOpen.Point3d(-12.526006869293845, 5.4558946256263585, 2.736656871093146)
    constraintReference29.HelpPoint = helpPoint28
    
    constraintReference29.SetFixHint(True)
    
    componentConstraint15.SetExpression("0")
    
    componentConstraint15.SetExpression("15.4645288351868")
    
    componentNetwork22.Solve()
    
    face32 = component2.FindObject("PROTO#.Features|BLEND(3)|FACE 7 {(-8.6506304676356,3.8535533905933,6.0542568085327) EXTRUDE(2)}")
    line40 = workPart.Lines.CreateFaceAxis(face32, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line40.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    face33 = component2.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 140 {(-8.6387728469369,0,6.2002225793082) EXTRUDE(2)}")
    line41 = workPart.Lines.CreateFaceAxis(face33, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line41.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    componentNetwork22.AddConstraint(componentConstraint15)
    
    expression174 = workPart.Expressions.FindObject("p8")
    expression174.RightHandSide = "1"
    
    objects42 = [NXOpen.TaggedObject.Null] * 1 
    objects42[0] = line40
    nErrs75 = theSession.UpdateManager.AddObjectsToDeleteList(objects42)
    
    objects43 = [NXOpen.TaggedObject.Null] * 1 
    objects43[0] = line41
    nErrs76 = theSession.UpdateManager.AddObjectsToDeleteList(objects43)
    
    componentNetwork22.Solve()
    
    rotMatrix6 = NXOpen.Matrix3x3()
    
    rotMatrix6.Xx = -0.074795486026383057
    rotMatrix6.Xy = 0.98543985147802171
    rotMatrix6.Xz = 0.15268901201153881
    rotMatrix6.Yx = -0.95967315071721815
    rotMatrix6.Yy = -0.11274131040038908
    rotMatrix6.Yz = 0.25752056368705495
    rotMatrix6.Zx = 0.27098538533023159
    rotMatrix6.Zy = -0.12727016951425119
    rotMatrix6.Zz = 0.95413270821686413
    translation39 = NXOpen.Point3d(6.4370613124680576, -9.1682947494978535, -1.3320471620877019)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation39, 8.0492656123141426)
    
    line42 = workPart.Lines.CreateFaceAxis(face32, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line42.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint112 = NXOpen.Point3d(13.67412531377788, 2.4324165221623972, 0.0)
    viewCenter112 = NXOpen.Point3d(-13.674125313777868, -2.4324165221624257, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint112, viewCenter112)
    
    scaleAboutPoint113 = NXOpen.Point3d(17.092656642222348, 3.0405206527029969, 0.0)
    viewCenter113 = NXOpen.Point3d(-17.092656642222337, -3.040520652703032, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint113, viewCenter113)
    
    scaleAboutPoint114 = NXOpen.Point3d(21.365820802777929, 3.800650815878754, 0.0)
    viewCenter114 = NXOpen.Point3d(-21.365820802777918, -3.8006508158787846, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint114, viewCenter114)
    
    scaleAboutPoint115 = NXOpen.Point3d(26.707276003472408, 4.7508135198484371, 0.0)
    viewCenter115 = NXOpen.Point3d(-26.707276003472398, -4.75081351984847, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint115, viewCenter115)
    
    scaleAboutPoint116 = NXOpen.Point3d(33.384095004340502, 5.9385168998105584, 0.0)
    viewCenter116 = NXOpen.Point3d(-33.384095004340502, -5.9385168998105859, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint116, viewCenter116)
    
    scaleAboutPoint117 = NXOpen.Point3d(41.730118755425643, 7.4231461247632078, 0.0)
    viewCenter117 = NXOpen.Point3d(-41.730118755425643, -7.4231461247632335, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint117, viewCenter117)
    
    scaleAboutPoint118 = NXOpen.Point3d(33.384095004340487, 5.9385168998105584, 0.0)
    viewCenter118 = NXOpen.Point3d(-33.384095004340502, -5.9385168998105859, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint118, viewCenter118)
    
    scaleAboutPoint119 = NXOpen.Point3d(26.707276003472394, 4.7508135198484425, 0.0)
    viewCenter119 = NXOpen.Point3d(-26.707276003472415, -4.75081351984847, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint119, viewCenter119)
    
    scaleAboutPoint120 = NXOpen.Point3d(21.365820802777922, 3.800650815878754, 0.0)
    viewCenter120 = NXOpen.Point3d(-21.365820802777922, -3.8006508158787757, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint120, viewCenter120)
    
    scaleAboutPoint121 = NXOpen.Point3d(17.092656642222341, 3.0405206527030031, 0.0)
    viewCenter121 = NXOpen.Point3d(-17.092656642222334, -3.040520652703024, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint121, viewCenter121)
    
    scaleAboutPoint122 = NXOpen.Point3d(13.674125313777868, 2.4324165221623963, 0.0)
    viewCenter122 = NXOpen.Point3d(-13.674125313777868, -2.4324165221624217, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint122, viewCenter122)
    
    scaleAboutPoint123 = NXOpen.Point3d(10.939300251022294, 1.9459332177299125, 0.0)
    viewCenter123 = NXOpen.Point3d(-10.939300251022294, -1.9459332177299418, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint123, viewCenter123)
    
    scaleAboutPoint124 = NXOpen.Point3d(8.7514402008178358, 1.5567465741839281, 0.0)
    viewCenter124 = NXOpen.Point3d(-8.7514402008178358, -1.5567465741839568, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint124, viewCenter124)
    
    scaleAboutPoint125 = NXOpen.Point3d(7.1357897022053125, 1.2622269520410183, 0.0)
    viewCenter125 = NXOpen.Point3d(-7.1357897022053125, -1.2622269520410501, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint125, viewCenter125)
    
    scaleAboutPoint126 = NXOpen.Point3d(5.708631761764245, 1.0097815616328101, 0.0)
    viewCenter126 = NXOpen.Point3d(-5.7086317617642521, -1.0097815616328434, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint126, viewCenter126)
    
    rotMatrix7 = NXOpen.Matrix3x3()
    
    rotMatrix7.Xx = -0.10982547881431515
    rotMatrix7.Xy = 0.99326357864956727
    rotMatrix7.Xz = 0.036957103937806685
    rotMatrix7.Yx = -0.94458216053902377
    rotMatrix7.Yy = -0.11587095813440414
    rotMatrix7.Yz = 0.30714567073695326
    rotMatrix7.Zx = 0.30935886312605632
    rotMatrix7.Zy = -0.0011766007304092226
    rotMatrix7.Zz = 0.9509446405633103
    translation40 = NXOpen.Point3d(-2.8218352703684721, -10.801626991426147, -0.89499574796442594)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix7, translation40, 24.564409217267283)
    
    scaleAboutPoint127 = NXOpen.Point3d(4.4591953761705607, 0.89399327589891309, 0.0)
    viewCenter127 = NXOpen.Point3d(-4.459195376170566, -0.89399327589894617, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint127, viewCenter127)
    
    scaleAboutPoint128 = NXOpen.Point3d(5.8298055491601843, 1.0501728240981227, 0.0)
    viewCenter128 = NXOpen.Point3d(-5.8298055491601888, -1.050172824098156, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint128, viewCenter128)
    
    scaleAboutPoint129 = NXOpen.Point3d(7.3377460145318727, 1.3127160301226579, 0.0)
    viewCenter129 = NXOpen.Point3d(-7.3377460145318754, -1.3127160301226923, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint129, viewCenter129)
    
    scaleAboutPoint130 = NXOpen.Point3d(10.329223890869123, 1.7250435011227323, 0.0)
    viewCenter130 = NXOpen.Point3d(-10.329223890869123, -1.7250435011227627, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint130, viewCenter130)
    
    componentNetwork22.AddConstraint(componentConstraint15)
    
    expression174.RightHandSide = "10"
    
    objects44 = [NXOpen.TaggedObject.Null] * 1 
    objects44[0] = line42
    nErrs77 = theSession.UpdateManager.AddObjectsToDeleteList(objects44)
    
    componentNetwork22.Solve()
    
    componentNetwork22.AddConstraint(componentConstraint15)
    
    expression174.RightHandSide = "-1"
    
    componentNetwork22.Solve()
    
    componentNetwork22.AddConstraint(componentConstraint15)
    
    expression174.RightHandSide = "-5"
    
    componentNetwork22.Solve()
    
    componentNetwork22.AddConstraint(componentConstraint15)
    
    expression174.RightHandSide = "-2"
    
    componentNetwork22.Solve()
    
    line43 = workPart.Lines.CreateFaceAxis(face23, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line43.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    line44 = workPart.Lines.CreateFaceAxis(face24, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line44.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    rotMatrix8 = NXOpen.Matrix3x3()
    
    rotMatrix8.Xx = 0.16828370333391746
    rotMatrix8.Xy = 0.95957144240727954
    rotMatrix8.Xz = -0.22561746853609799
    rotMatrix8.Yx = -0.18651223256274851
    rotMatrix8.Yy = 0.25574306439942868
    rotMatrix8.Yz = 0.9485824540418466
    rotMatrix8.Zx = 0.96793273645263411
    rotMatrix8.Zy = -0.11755055052191463
    rotMatrix8.Zz = 0.22200920200593866
    translation41 = NXOpen.Point3d(6.6949121646967011, -4.0468849414252919, 5.1998520647439666)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix8, translation41, 10.06158201539268)
    
    objects45 = [NXOpen.TaggedObject.Null] * 1 
    objects45[0] = line44
    nErrs78 = theSession.UpdateManager.AddObjectsToDeleteList(objects45)
    
    objects46 = [NXOpen.TaggedObject.Null] * 1 
    objects46[0] = line43
    nErrs79 = theSession.UpdateManager.AddObjectsToDeleteList(objects46)
    
    markId100 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs80 = theSession.UpdateManager.DoUpdate(markId98)
    
    componentNetwork22.Solve()
    
    componentPositioner22.ClearNetwork()
    
    nErrs81 = theSession.UpdateManager.AddToDeleteList(componentNetwork22)
    
    componentPositioner22.DeleteNonPersistentConstraints()
    
    nErrs82 = theSession.UpdateManager.DoUpdate(markId98)
    
    theSession.DeleteUndoMark(markId100, None)
    
    theSession.SetUndoMarkName(markId97, "Assembly Constraints")
    
    componentPositioner22.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner22.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId98, None)
    
    theSession.DeleteUndoMark(markId99, None)
    
    markId101 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner23 = workPart.ComponentAssembly.Positioner
    
    componentPositioner23.ClearNetwork()
    
    componentPositioner23.PrimaryArrangement = arrangement1
    
    componentPositioner23.BeginAssemblyConstraints()
    
    allowInterpartPositioning22 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression175 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression176 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression177 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression178 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression179 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression180 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression181 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression182 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network23 = componentPositioner23.EstablishNetwork()
    
    componentNetwork23 = network23
    componentNetwork23.MoveObjectsState = True
    
    componentNetwork23.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork23.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId101, "Assembly Constraints Dialog")
    
    componentNetwork23.MoveObjectsState = True
    
    componentNetwork23.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId102 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   Dialog Begin Assembly Constraints
    # ----------------------------------------------
    rotMatrix9 = NXOpen.Matrix3x3()
    
    rotMatrix9.Xx = 0.1329495560746522
    rotMatrix9.Xy = 0.9907811236027122
    rotMatrix9.Xz = 0.026022694943167737
    rotMatrix9.Yx = -0.44820982655433533
    rotMatrix9.Yy = 0.036684659418214818
    rotMatrix9.Yz = 0.89317533952942751
    rotMatrix9.Zx = 0.88398663277206346
    rotMatrix9.Zy = -0.13041089247421719
    rotMatrix9.Zz = 0.44895504474768139
    translation42 = NXOpen.Point3d(5.8831724326499995, -7.024618456958895, 3.8577505624085644)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix9, translation42, 10.06158201539268)
    
    line45 = workPart.Lines.CreateFaceAxis(face7, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line45.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    rotMatrix10 = NXOpen.Matrix3x3()
    
    rotMatrix10.Xx = -0.32309252077432588
    rotMatrix10.Xy = 0.91220461608180936
    rotMatrix10.Xz = -0.25198008139282679
    rotMatrix10.Yx = -0.66794187130780969
    rotMatrix10.Yy = -0.031182412589839316
    rotMatrix10.Yz = 0.74355989247598919
    rotMatrix10.Zx = 0.67042141938747712
    rotMatrix10.Zy = 0.40854668710457182
    rotMatrix10.Zz = 0.61937446256878104
    translation43 = NXOpen.Point3d(3.067146043660764, -8.5155673681131709, 5.1124010662220467)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix10, translation43, 10.06158201539268)
    
    scaleAboutPoint131 = NXOpen.Point3d(-0.63111347602051682, -4.7596474649880784, 0.0)
    viewCenter131 = NXOpen.Point3d(0.63111347602051682, 4.7596474649880491, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint131, viewCenter131)
    
    scaleAboutPoint132 = NXOpen.Point3d(-0.90459598229607474, -3.5763096974496094, 0.0)
    viewCenter132 = NXOpen.Point3d(0.90459598229607474, 3.5763096974495805, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint132, viewCenter132)
    
    scaleAboutPoint133 = NXOpen.Point3d(-0.90880340546954441, -2.8442180652658098, 0.0)
    viewCenter133 = NXOpen.Point3d(0.90880340546954297, 2.8442180652657809, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint133, viewCenter133)
    
    scaleAboutPoint134 = NXOpen.Point3d(-1.0771003324083519, -2.2753744522126511, 0.0)
    viewCenter134 = NXOpen.Point3d(1.0771003324083475, 2.2753744522126227, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint134, viewCenter134)
    
    objects47 = [NXOpen.TaggedObject.Null] * 1 
    objects47[0] = line45
    nErrs83 = theSession.UpdateManager.AddObjectsToDeleteList(objects47)
    
    scaleAboutPoint135 = NXOpen.Point3d(2.2834527047056969, -1.324833408862284, 0.0)
    viewCenter135 = NXOpen.Point3d(-2.2834527047057005, 1.3248334088622555, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint135, viewCenter135)
    
    scaleAboutPoint136 = NXOpen.Point3d(2.8677796350372269, -1.6560417610778513, 0.0)
    viewCenter136 = NXOpen.Point3d(-2.8677796350372313, 1.6560417610778226, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint136, viewCenter136)
    
    face34 = component2.FindObject("PROTO#.Features|BLEND(3)|FACE 11 {(-2.1271945210511,-3.8535533905933,2.5082775225319) EXTRUDE(2)}")
    line46 = workPart.Lines.CreateFaceAxis(face34, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line46.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint137 = NXOpen.Point3d(3.5847245437965332, -2.0700522013473099, 0.0)
    viewCenter137 = NXOpen.Point3d(-3.5847245437965389, 2.0700522013472811, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint137, viewCenter137)
    
    scaleAboutPoint138 = NXOpen.Point3d(4.5019427956130196, -2.5875652516841359, 0.0)
    viewCenter138 = NXOpen.Point3d(-4.5019427956130231, 2.5875652516841035, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint138, viewCenter138)
    
    markId103 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint16 = componentPositioner23.CreateConstraint(True)
    
    componentConstraint16 = constraint16
    componentConstraint16.ConstraintType = NXOpen.Positioning.Constraint.Type.Distance
    
    constraintReference30 = componentConstraint16.CreateConstraintReference(component16, face26, False, False, False)
    
    helpPoint29 = NXOpen.Point3d(-5.4488703230638196, -7.5242516565748421, 0.01549824592047026)
    constraintReference30.HelpPoint = helpPoint29
    
    constraintReference31 = componentConstraint16.CreateConstraintReference(component2, face31, False, False, False)
    
    helpPoint30 = NXOpen.Point3d(-7.9297760435253011, 5.4558946256263585, 1.5617805524925643)
    constraintReference31.HelpPoint = helpPoint30
    
    constraintReference31.SetFixHint(True)
    
    componentConstraint16.SetExpression("0")
    
    componentConstraint16.SetExpression("12.9801462822087")
    
    objects48 = [NXOpen.TaggedObject.Null] * 1 
    objects48[0] = line46
    nErrs84 = theSession.UpdateManager.AddObjectsToDeleteList(objects48)
    
    componentNetwork23.Solve()
    
    line47 = workPart.Lines.CreateFaceAxis(face32, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line47.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    line48 = workPart.Lines.CreateFaceAxis(face33, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line48.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    componentNetwork23.AddConstraint(componentConstraint16)
    
    expression183 = workPart.Expressions.FindObject("p17")
    expression183.RightHandSide = "-2"
    
    objects49 = [NXOpen.TaggedObject.Null] * 1 
    objects49[0] = line47
    nErrs85 = theSession.UpdateManager.AddObjectsToDeleteList(objects49)
    
    objects50 = [NXOpen.TaggedObject.Null] * 1 
    objects50[0] = line48
    nErrs86 = theSession.UpdateManager.AddObjectsToDeleteList(objects50)
    
    componentNetwork23.Solve()
    
    markId104 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs87 = theSession.UpdateManager.DoUpdate(markId102)
    
    componentNetwork23.Solve()
    
    componentPositioner23.ClearNetwork()
    
    nErrs88 = theSession.UpdateManager.AddToDeleteList(componentNetwork23)
    
    componentPositioner23.DeleteNonPersistentConstraints()
    
    nErrs89 = theSession.UpdateManager.DoUpdate(markId102)
    
    theSession.DeleteUndoMark(markId104, None)
    
    theSession.SetUndoMarkName(markId101, "Assembly Constraints")
    
    componentPositioner23.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner23.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId102, None)
    
    theSession.DeleteUndoMark(markId103, None)
    
    markId105 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner24 = workPart.ComponentAssembly.Positioner
    
    componentPositioner24.ClearNetwork()
    
    componentPositioner24.PrimaryArrangement = arrangement1
    
    componentPositioner24.BeginAssemblyConstraints()
    
    allowInterpartPositioning23 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression184 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression185 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression186 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression187 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression188 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression189 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression190 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression191 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network24 = componentPositioner24.EstablishNetwork()
    
    componentNetwork24 = network24
    componentNetwork24.MoveObjectsState = True
    
    componentNetwork24.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork24.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId105, "Assembly Constraints Dialog")
    
    componentNetwork24.MoveObjectsState = True
    
    componentNetwork24.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId106 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   Dialog Begin Assembly Constraints
    # ----------------------------------------------
    rotMatrix11 = NXOpen.Matrix3x3()
    
    rotMatrix11.Xx = 0.75884560848840377
    rotMatrix11.Xy = 0.64940052344927424
    rotMatrix11.Xz = 0.049318380160704924
    rotMatrix11.Yx = -0.44264070873336014
    rotMatrix11.Yy = 0.45872635570345965
    rotMatrix11.Yz = 0.77047993715284679
    rotMatrix11.Zx = 0.47772643369390427
    rotMatrix11.Zy = -0.6065056394847741
    rotMatrix11.Zz = 0.63555358847486165
    translation44 = NXOpen.Point3d(14.09309959361163, -6.9594660222902558, 5.2001915656952971)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix11, translation44, 10.06158201539268)
    
    componentPositioner24.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner24.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId106, None)
    
    theSession.UndoToMark(markId105, None)
    
    theSession.DeleteUndoMark(markId105, None)
    
    theSession.DeleteUndoMark(markId96, None)
    
    # ----------------------------------------------
    #   Menu: File->Open...
    # ----------------------------------------------
    try:
        # File already exists
        basePart6, partLoadStatus8 = theSession.Parts.OpenActiveDisplay("C:\\Users\\Admin\\Desktop\\機器人組裝\車二.prt\\車二.prt", NXOpen.DisplayPartOption.AllowAdditional)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1020004)
        
    markId107 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    status3, partLoadStatus9 = theSession.Parts.SetActiveDisplay(part5, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = theSession.Parts.Work # 車二
    displayPart = theSession.Parts.Display # 車二
    partLoadStatus9.Dispose()
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit Parameters...
    # ----------------------------------------------
    markId108 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    # User Function call - UF_PART_ask_part_name
    
    markId109 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    extrude1 = workPart.Features.FindObject("EXTRUDE(2)")
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(extrude1)
    
    section2 = extrudeBuilder1.Section
    
    section2.PrepareMappingData()
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit6 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression192 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit6)
    
    unit7 = extrudeBuilder1.Offset.StartOffset.Units
    
    expression193 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit7)
    
    expression194 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit7)
    
    theSession.SetUndoMarkName(markId109, "Extrude Dialog")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    markId110 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId111 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId111, None)
    
    workPart.Expressions.Delete(expression193)
    
    workPart.Expressions.Delete(expression194)
    
    expression195 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit7)
    
    expression196 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit7)
    
    theSession.DeleteUndoMark(markId110, None)
    
    expression197 = workPart.Expressions.FindObject("p1")
    expression197.SetFormula("2.5")
    
    sketchFeature2 = workPart.Features.FindObject("SKETCH(1)")
    sketch2 = sketchFeature2.FindObject("SKETCH_000")
    sketch2.LocalUpdate()
    
    markId112 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId112, None)
    
    markId113 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    feature2 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId113, None)
    
    theSession.SetUndoMarkName(markId109, "Extrude")
    
    section2.CleanMappingData()
    
    expression198 = extrudeBuilder1.Limits.StartExtend.Value
    expression199 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression192)
    
    workPart.Expressions.Delete(expression195)
    
    workPart.Expressions.Delete(expression196)
    
    theSession.DeleteUndoMark(markId109, None)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    nErrs90 = theSession.UpdateManager.DoUpdate(markId108)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    # ----------------------------------------------
    #   Menu: File->Save
    # ----------------------------------------------
    partSaveStatus2 = workPart.Save(NXOpen.BasePart.SaveComponents.TrueValue, NXOpen.BasePart.CloseAfterSave.FalseValue)
    
    partSaveStatus2.Dispose()
    markId114 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Undisplay Part")
    
    workPart.Undisplay()
    
    workPart = NXOpen.Part.Null
    displayPart = NXOpen.Part.Null
    markId115 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    status4, partLoadStatus10 = theSession.Parts.SetActiveDisplay(part3, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = theSession.Parts.Work # assembly1
    displayPart = theSession.Parts.Display # assembly1
    partLoadStatus10.Dispose()
    rotMatrix12 = NXOpen.Matrix3x3()
    
    rotMatrix12.Xx = 0.44103238896241342
    rotMatrix12.Xy = 0.89698472098577919
    rotMatrix12.Xz = -0.030147009871199622
    rotMatrix12.Yx = -0.40289473708494672
    rotMatrix12.Yy = 0.22788858454584646
    rotMatrix12.Yz = 0.88642124515545562
    rotMatrix12.Zx = 0.80197647266946959
    rotMatrix12.Zy = -0.37879440776199397
    rotMatrix12.Zz = 0.46189667019029707
    translation45 = NXOpen.Point3d(11.738299086730065, -6.6651268676122557, 7.6030551418872623)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix12, translation45, 10.061582015392688)
    
    # ----------------------------------------------
    #   Menu: File->Open...
    # ----------------------------------------------
    try:
        # File already exists
        basePart7, partLoadStatus11 = theSession.Parts.OpenActiveDisplay("C:\\Users\\Admin\\Desktop\\機器人組裝\車三.prt\\車三.prt", NXOpen.DisplayPartOption.AllowAdditional)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1020004)
        
    markId116 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    status5, partLoadStatus12 = theSession.Parts.SetActiveDisplay(part4, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = theSession.Parts.Work # 車三
    displayPart = theSession.Parts.Display # 車三
    partLoadStatus12.Dispose()
    # ----------------------------------------------
    #   Menu: Edit->Feature->Edit Parameters...
    # ----------------------------------------------
    markId117 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    # User Function call - UF_PART_ask_part_name
    
    markId118 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    revolve2 = workPart.Features.FindObject("REVOLVED(1)")
    revolveBuilder2 = workPart.Features.CreateRevolveBuilder(revolve2)
    
    section3 = revolveBuilder2.Section
    
    section3.PrepareMappingData()
    
    unit8 = revolveBuilder2.Offset.StartOffset.Units
    
    expression200 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit8)
    
    theSession.SetUndoMarkName(markId118, "Revolve Dialog")
    
    sketchFeature3 = workPart.Features.FindObject("REVOLVED(1:1B)")
    revolveBuilder2.ShowInternalParentFeatureForEdit(sketchFeature3)
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    markId119 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId120 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId120, None)
    
    revolveBuilder2.Section = section3
    
    workPart.Expressions.Delete(expression200)
    
    expression201 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit8)
    
    theSession.DeleteUndoMark(markId119, None)
    
    expression202 = workPart.Expressions.FindObject("p5")
    expression202.SetFormula("10")
    
    sketch3 = sketchFeature3.FindObject("SKETCH_000")
    sketch3.LocalUpdate()
    
    revolveBuilder2.Section = section3
    
    markId121 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    
    theSession.DeleteUndoMark(markId121, None)
    
    markId122 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Revolve")
    
    feature3 = revolveBuilder2.CommitFeature()
    
    theSession.DeleteUndoMark(markId122, None)
    
    theSession.SetUndoMarkName(markId118, "Revolve")
    
    section3.CleanMappingData()
    
    expression203 = revolveBuilder2.Limits.StartExtend.Value
    expression204 = revolveBuilder2.Limits.EndExtend.Value
    revolveBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression201)
    
    theSession.DeleteUndoMark(markId118, None)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    nErrs91 = theSession.UpdateManager.DoUpdate(markId117)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    # ----------------------------------------------
    #   Menu: File->Save
    # ----------------------------------------------
    partSaveStatus3 = workPart.Save(NXOpen.BasePart.SaveComponents.TrueValue, NXOpen.BasePart.CloseAfterSave.FalseValue)
    
    partSaveStatus3.Dispose()
    markId123 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Change Displayed Part")
    
    status6, partLoadStatus13 = theSession.Parts.SetActiveDisplay(part3, NXOpen.DisplayPartOption.AllowAdditional, NXOpen.PartDisplayPartWorkPartOption.UseLast)
    
    workPart = theSession.Parts.Work # assembly1
    displayPart = theSession.Parts.Display # assembly1
    partLoadStatus13.Dispose()
    theSession.DeleteUndoMark(markId123, None)
    
    rotMatrix13 = NXOpen.Matrix3x3()
    
    rotMatrix13.Xx = 0.20354224866060783
    rotMatrix13.Xy = 0.97906322061486029
    rotMatrix13.Xz = -0.0024006352170408037
    rotMatrix13.Yx = -0.76017267043576553
    rotMatrix13.Yy = 0.15958031764037897
    rotMatrix13.Yz = 0.62981873054424087
    rotMatrix13.Zx = 0.61701544886068127
    rotMatrix13.Zy = -0.12636982337986535
    rotMatrix13.Zz = 0.77673843963473488
    translation46 = NXOpen.Point3d(9.8071158101352172, -8.2799370311295846, 4.8306845030802741)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix13, translation46, 10.061582015392688)
    
    scaleAboutPoint139 = NXOpen.Point3d(13.253382996430858, 0.49963150184956107, 0.0)
    viewCenter139 = NXOpen.Point3d(-13.253382996430858, -0.49963150184959243, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint139, viewCenter139)
    
    scaleAboutPoint140 = NXOpen.Point3d(21.23433882860698, -1.3805607287948922, 0.0)
    viewCenter140 = NXOpen.Point3d(-21.23433882860698, 1.3805607287948671, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint140, viewCenter140)
    
    scaleAboutPoint141 = NXOpen.Point3d(16.987471062885582, -1.1044485830359183, 0.0)
    viewCenter141 = NXOpen.Point3d(-16.987471062885582, 1.1044485830358892, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint141, viewCenter141)
    
    scaleAboutPoint142 = NXOpen.Point3d(13.589976850308464, -0.88355886642873838, 0.0)
    viewCenter142 = NXOpen.Point3d(-13.589976850308471, 0.88355886642870962, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint142, viewCenter142)
    
    markId124 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Constraints with Positioning Task")
    
    markId125 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner25 = workPart.ComponentAssembly.Positioner
    
    componentPositioner25.ClearNetwork()
    
    componentPositioner25.PrimaryArrangement = arrangement1
    
    componentPositioner25.BeginAssemblyConstraints()
    
    allowInterpartPositioning24 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression205 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression206 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression207 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression208 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression209 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression210 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression211 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression212 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network25 = componentPositioner25.EstablishNetwork()
    
    componentNetwork25 = network25
    componentNetwork25.MoveObjectsState = True
    
    componentNetwork25.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork25.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId125, "Assembly Constraints Dialog")
    
    componentNetwork25.AddConstraint(componentConstraint15)
    
    loaded3 = componentNetwork25.IsReferencedGeometryLoaded()
    
    componentNetwork25.AddConstraint(componentConstraint15)
    
    loaded4 = componentNetwork25.IsReferencedGeometryLoaded()
    
    componentNetwork25.MoveObjectsState = True
    
    componentNetwork25.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId126 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    componentNetwork25.AddConstraint(componentConstraint15)
    
    expression174.RightHandSide = "-2"
    
    componentNetwork25.Solve()
    
    line49 = workPart.Lines.CreateFaceAxis(face6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line49.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    componentNetwork25.AddConstraint(componentConstraint15)
    
    expression174.RightHandSide = "-1"
    
    objects51 = [NXOpen.TaggedObject.Null] * 1 
    objects51[0] = line49
    nErrs92 = theSession.UpdateManager.AddObjectsToDeleteList(objects51)
    
    componentNetwork25.Solve()
    
    rotMatrix14 = NXOpen.Matrix3x3()
    
    rotMatrix14.Xx = 0.10114658483015003
    rotMatrix14.Xy = 0.9867215201698043
    rotMatrix14.Xz = -0.12708268965910779
    rotMatrix14.Yx = -0.45678719417221297
    rotMatrix14.Yy = 0.15953770945721688
    rotMatrix14.Yz = 0.87515323144088764
    rotMatrix14.Zx = 0.88380700812874424
    rotMatrix14.Zy = -0.030469015326075551
    rotMatrix14.Zz = 0.46685844909092755
    translation47 = NXOpen.Point3d(2.3727041179611472, -6.0429126794645898, 7.3516284395319813)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix14, translation47, 15.721221899051073)
    
    face35 = component2.FindObject("PROTO#.Features|BLEND(3)|FACE 8 {(-8.6506304676356,-3.8535533905933,6.0542568085327) EXTRUDE(2)}")
    line50 = workPart.Lines.CreateFaceAxis(face35, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line50.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint143 = NXOpen.Point3d(-1.3127160301226812, 0.4712313954286389, 0.0)
    viewCenter143 = NXOpen.Point3d(1.3127160301226699, -0.4712313954286676, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint143, viewCenter143)
    
    scaleAboutPoint144 = NXOpen.Point3d(-1.6198579217859987, 0.52592789668375051, 0.0)
    viewCenter144 = NXOpen.Point3d(1.6198579217859916, -0.52592789668377926, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint144, viewCenter144)
    
    scaleAboutPoint145 = NXOpen.Point3d(7.1000266052308136, 0.71000266052306837, 0.0)
    viewCenter145 = NXOpen.Point3d(-7.1000266052308225, -0.71000266052309524, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint145, viewCenter145)
    
    scaleAboutPoint146 = NXOpen.Point3d(5.5748357048478967, 0.58903924428580223, 0.0)
    viewCenter146 = NXOpen.Point3d(-5.5748357048479038, -0.58903924428583088, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint146, viewCenter146)
    
    line51 = workPart.Lines.CreateFaceAxis(face32, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line51.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    rotMatrix15 = NXOpen.Matrix3x3()
    
    rotMatrix15.Xx = 0.095607081804909538
    rotMatrix15.Xy = 0.9870297097144306
    rotMatrix15.Xz = -0.12896370826632378
    rotMatrix15.Yx = -0.48722047320196626
    rotMatrix15.Yy = 0.15937870858314407
    rotMatrix15.Yz = 0.85861204146181636
    rotMatrix15.Zx = 0.86802966331895004
    rotMatrix15.Zy = -0.019255632719323543
    rotMatrix15.Zz = 0.49613881546093347
    translation48 = NXOpen.Point3d(-0.92941401490938191, -6.2195633986004237, 7.1394329236452423)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix15, translation48, 15.721221899051073)
    
    line52 = workPart.Lines.CreateFaceAxis(face33, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line52.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    objects52 = [NXOpen.TaggedObject.Null] * 1 
    objects52[0] = line51
    nErrs93 = theSession.UpdateManager.AddObjectsToDeleteList(objects52)
    
    objects53 = [NXOpen.TaggedObject.Null] * 1 
    objects53[0] = line50
    nErrs94 = theSession.UpdateManager.AddObjectsToDeleteList(objects53)
    
    objects54 = [NXOpen.TaggedObject.Null] * 1 
    objects54[0] = line52
    nErrs95 = theSession.UpdateManager.AddObjectsToDeleteList(objects54)
    
    markId127 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs96 = theSession.UpdateManager.DoUpdate(markId126)
    
    componentNetwork25.Solve()
    
    componentPositioner25.ClearNetwork()
    
    nErrs97 = theSession.UpdateManager.AddToDeleteList(componentNetwork25)
    
    componentPositioner25.DeleteNonPersistentConstraints()
    
    nErrs98 = theSession.UpdateManager.DoUpdate(markId126)
    
    theSession.DeleteUndoMark(markId127, None)
    
    theSession.SetUndoMarkName(markId125, "Assembly Constraints")
    
    componentPositioner25.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner25.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId126, None)
    
    markId128 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner26 = workPart.ComponentAssembly.Positioner
    
    componentPositioner26.ClearNetwork()
    
    componentPositioner26.PrimaryArrangement = arrangement1
    
    componentPositioner26.BeginAssemblyConstraints()
    
    allowInterpartPositioning25 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression213 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression214 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression215 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression216 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression217 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression218 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression219 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression220 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network26 = componentPositioner26.EstablishNetwork()
    
    componentNetwork26 = network26
    componentNetwork26.MoveObjectsState = True
    
    componentNetwork26.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork26.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId128, "Assembly Constraints Dialog")
    
    componentNetwork26.MoveObjectsState = True
    
    componentNetwork26.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId129 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   Dialog Begin Assembly Constraints
    # ----------------------------------------------
    line53 = workPart.Lines.CreateFaceAxis(face23, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line53.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    line54 = workPart.Lines.CreateFaceAxis(face16, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line54.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    line55 = workPart.Lines.CreateFaceAxis(face24, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line55.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId130 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Constraint")
    
    objects55 = [NXOpen.TaggedObject.Null] * 1 
    objects55[0] = line54
    nErrs99 = theSession.UpdateManager.AddObjectsToDeleteList(objects55)
    
    objects56 = [NXOpen.TaggedObject.Null] * 1 
    objects56[0] = line55
    nErrs100 = theSession.UpdateManager.AddObjectsToDeleteList(objects56)
    
    objects57 = [NXOpen.TaggedObject.Null] * 1 
    objects57[0] = line53
    nErrs101 = theSession.UpdateManager.AddObjectsToDeleteList(objects57)
    
    componentNetwork26.AddConstraint(componentConstraint16)
    
    loaded5 = componentNetwork26.IsReferencedGeometryLoaded()
    
    line56 = workPart.Lines.CreateFaceAxis(face24, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line56.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    line57 = workPart.Lines.CreateFaceAxis(face16, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line57.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    componentNetwork26.AddConstraint(componentConstraint16)
    
    expression183.RightHandSide = "-1"
    
    objects58 = [NXOpen.TaggedObject.Null] * 1 
    objects58[0] = line57
    nErrs102 = theSession.UpdateManager.AddObjectsToDeleteList(objects58)
    
    objects59 = [NXOpen.TaggedObject.Null] * 1 
    objects59[0] = line56
    nErrs103 = theSession.UpdateManager.AddObjectsToDeleteList(objects59)
    
    componentNetwork26.Solve()
    
    markId131 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints")
    
    nErrs104 = theSession.UpdateManager.DoUpdate(markId129)
    
    componentNetwork26.Solve()
    
    componentPositioner26.ClearNetwork()
    
    nErrs105 = theSession.UpdateManager.AddToDeleteList(componentNetwork26)
    
    componentPositioner26.DeleteNonPersistentConstraints()
    
    nErrs106 = theSession.UpdateManager.DoUpdate(markId129)
    
    theSession.DeleteUndoMark(markId131, None)
    
    theSession.SetUndoMarkName(markId128, "Assembly Constraints")
    
    componentPositioner26.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner26.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId129, None)
    
    theSession.DeleteUndoMark(markId130, None)
    
    markId132 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner27 = workPart.ComponentAssembly.Positioner
    
    componentPositioner27.ClearNetwork()
    
    componentPositioner27.PrimaryArrangement = arrangement1
    
    componentPositioner27.BeginAssemblyConstraints()
    
    allowInterpartPositioning26 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression221 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression222 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression223 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit3)
    
    expression224 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit4)
    
    expression225 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression226 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit3)
    
    expression227 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit3)
    
    expression228 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit4)
    
    network27 = componentPositioner27.EstablishNetwork()
    
    componentNetwork27 = network27
    componentNetwork27.MoveObjectsState = True
    
    componentNetwork27.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork27.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId132, "Assembly Constraints Dialog")
    
    componentNetwork27.MoveObjectsState = True
    
    componentNetwork27.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId133 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   Dialog Begin Assembly Constraints
    # ----------------------------------------------
    rotMatrix16 = NXOpen.Matrix3x3()
    
    rotMatrix16.Xx = 0.66935096965598351
    rotMatrix16.Xy = 0.74289736488111746
    rotMatrix16.Xz = -0.0085313933968601107
    rotMatrix16.Yx = -0.36763662696254973
    rotMatrix16.Yy = 0.3411758766274457
    rotMatrix16.Yz = 0.86512561615241734
    rotMatrix16.Zx = 0.64561024615181095
    rotMatrix16.Zy = -0.57593621735413691
    rotMatrix16.Zz = 0.50148268524807149
    translation49 = NXOpen.Point3d(3.0896212672251639, -5.6695924631098276, 6.3867470530420203)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix16, translation49, 15.721221899051073)
    
    line58 = workPart.Lines.CreateFaceAxis(face9, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line58.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    componentPositioner27.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner27.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId133, None)
    
    objects60 = [NXOpen.TaggedObject.Null] * 1 
    objects60[0] = line58
    nErrs107 = theSession.UpdateManager.AddObjectsToDeleteList(objects60)
    
    theSession.UndoToMark(markId132, None)
    
    theSession.DeleteUndoMark(markId132, None)
    
    theSession.DeleteUndoMark(markId124, None)
    
    scaleAboutPoint147 = NXOpen.Point3d(-3.5678948511026594, 1.0939300251022162, 0.0)
    viewCenter147 = NXOpen.Point3d(3.5678948511026567, -1.0939300251022448, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint147, viewCenter147)
    
    scaleAboutPoint148 = NXOpen.Point3d(-2.8543158808821301, 0.87514402008177061, 0.0)
    viewCenter148 = NXOpen.Point3d(2.8543158808821256, -0.87514402008179826, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint148, viewCenter148)
    
    scaleAboutPoint149 = NXOpen.Point3d(-2.2295976880852857, 0.70011521606541371, 0.0)
    viewCenter149 = NXOpen.Point3d(2.2295976880852821, -0.70011521606544214, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint149, viewCenter149)
    
    scaleAboutPoint150 = NXOpen.Point3d(-1.7750613478089621, 0.56870897551159316, 0.0)
    viewCenter150 = NXOpen.Point3d(1.7750613478089585, -0.56870897551162336, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint150, viewCenter150)
    
    scaleAboutPoint151 = NXOpen.Point3d(-1.4131556361197568, 0.45496718040927209, 0.0)
    viewCenter151 = NXOpen.Point3d(1.4131556361197521, -0.45496718040930145, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint151, viewCenter151)
    
    scaleAboutPoint152 = NXOpen.Point3d(-1.7664445451496937, 0.56870897551159461, 0.0)
    viewCenter152 = NXOpen.Point3d(1.7664445451496915, -0.56870897551162258, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint152, viewCenter152)
    
    scaleAboutPoint153 = NXOpen.Point3d(-2.2080556814371164, 0.71088621938949492, 0.0)
    viewCenter153 = NXOpen.Point3d(2.2080556814371164, -0.71088621938952434, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint153, viewCenter153)
    
    scaleAboutPoint154 = NXOpen.Point3d(-2.7600696017963977, 0.88860777423687443, 0.0)
    viewCenter154 = NXOpen.Point3d(2.7600696017963933, -0.88860777423690307, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint154, viewCenter154)
    
    scaleAboutPoint155 = NXOpen.Point3d(-3.4500870022454966, 1.1107597177960957, 0.0)
    viewCenter155 = NXOpen.Point3d(3.4500870022454908, -1.1107597177961259, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint155, viewCenter155)
    
    scaleAboutPoint156 = NXOpen.Point3d(-4.3126087528068711, 1.3884496472451233, 0.0)
    viewCenter156 = NXOpen.Point3d(4.312608752806864, -1.388449647245152, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint156, viewCenter156)
    
    rotMatrix17 = NXOpen.Matrix3x3()
    
    rotMatrix17.Xx = 0.80207532253358127
    rotMatrix17.Xy = 0.58213816704632049
    rotMatrix17.Xz = -0.13338040129870041
    rotMatrix17.Yx = -0.26855569238753457
    rotMatrix17.Yy = 0.55104326091629319
    rotMatrix17.Yz = 0.79008174557129818
    rotMatrix17.Zx = 0.53343511045759273
    rotMatrix17.Zy = -0.59788500488529328
    rotMatrix17.Zz = 0.59831471974572692
    translation50 = NXOpen.Point3d(2.698373385120524, -4.4462070401822213, 5.3717820379747501)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix17, translation50, 10.061582015392688)
    
    # ----------------------------------------------
    #   Menu: File->Save
    # ----------------------------------------------
    markId134 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId134, "Name Parts Dialog")
    
    markId135 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Name Parts")
    
    theSession.DeleteUndoMark(markId135, None)
    
    markId136 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Name Parts")
    
    workPart.AssignPermanentName("C:\\Users\\Admin\\Desktop\\機器人組裝\組合.prt\\組合.prt")
    
    theSession.DeleteUndoMark(markId136, None)
    
    theSession.SetUndoMarkName(markId134, "Name Parts")
    
    partSaveStatus4 = workPart.Save(NXOpen.BasePart.SaveComponents.TrueValue, NXOpen.BasePart.CloseAfterSave.FalseValue)
    
    partSaveStatus4.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()