Search.setIndex({docnames:["augment_to_disk_example","dataloader_example","examples","ida_lib","ida_lib.core","ida_lib.image_augmentation","ida_lib.operations","index","neural_net_example","overview","pipeline_example","transformations"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":2,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,sphinx:56},filenames:["augment_to_disk_example.rst","dataloader_example.rst","examples.rst","ida_lib.rst","ida_lib.core.rst","ida_lib.image_augmentation.rst","ida_lib.operations.rst","index.rst","neural_net_example.rst","overview.rst","pipeline_example.rst","transformations.rst"],objects:{"ida_lib.core":{pipeline:[4,0,0,"-"],pipeline_functional:[4,0,0,"-"],pipeline_geometric_ops:[4,0,0,"-"],pipeline_local_ops:[4,0,0,"-"],pipeline_operations:[4,0,0,"-"],pipeline_pixel_ops:[4,0,0,"-"]},"ida_lib.core.pipeline":{Pipeline:[4,1,1,""]},"ida_lib.core.pipeline.Pipeline":{get_data_types:[4,2,1,""]},"ida_lib.core.pipeline_functional":{get_compose_function:[4,3,1,""],get_compose_matrix:[4,3,1,""],postprocess_data:[4,3,1,""],preprocess_data:[4,3,1,""],split_operations_by_type:[4,3,1,""],switch_point_positions:[4,3,1,""]},"ida_lib.core.pipeline_geometric_ops":{HflipPipeline:[4,1,1,""],RandomRotatePipeline:[4,1,1,""],RandomScalePipeline:[4,1,1,""],RandomShearPipeline:[4,1,1,""],RandomTranslatePipeline:[4,1,1,""],RotatePipeline:[4,1,1,""],ScalePipeline:[4,1,1,""],ShearPipeline:[4,1,1,""],TranslatePipeline:[4,1,1,""],VflipPipeline:[4,1,1,""]},"ida_lib.core.pipeline_geometric_ops.HflipPipeline":{config_parameters:[4,2,1,""],get_op_matrix:[4,2,1,""],need_data_info:[4,2,1,""],switch_points:[4,2,1,""]},"ida_lib.core.pipeline_geometric_ops.RandomRotatePipeline":{config_parameters:[4,2,1,""],get_op_matrix:[4,2,1,""],need_data_info:[4,2,1,""],switch_points:[4,2,1,""]},"ida_lib.core.pipeline_geometric_ops.RandomScalePipeline":{config_parameters:[4,2,1,""],get_op_matrix:[4,2,1,""],need_data_info:[4,2,1,""],switch_points:[4,2,1,""]},"ida_lib.core.pipeline_geometric_ops.RandomShearPipeline":{get_op_matrix:[4,2,1,""],need_data_info:[4,2,1,""],switch_points:[4,2,1,""]},"ida_lib.core.pipeline_geometric_ops.RandomTranslatePipeline":{get_op_matrix:[4,2,1,""],need_data_info:[4,2,1,""],switch_points:[4,2,1,""]},"ida_lib.core.pipeline_geometric_ops.RotatePipeline":{config_parameters:[4,2,1,""],get_op_matrix:[4,2,1,""],need_data_info:[4,2,1,""],switch_points:[4,2,1,""]},"ida_lib.core.pipeline_geometric_ops.ScalePipeline":{config_parameters:[4,2,1,""],get_op_matrix:[4,2,1,""],need_data_info:[4,2,1,""],switch_points:[4,2,1,""]},"ida_lib.core.pipeline_geometric_ops.ShearPipeline":{get_op_matrix:[4,2,1,""],need_data_info:[4,2,1,""],switch_points:[4,2,1,""]},"ida_lib.core.pipeline_geometric_ops.TranslatePipeline":{get_op_matrix:[4,2,1,""],need_data_info:[4,2,1,""],switch_points:[4,2,1,""]},"ida_lib.core.pipeline_geometric_ops.VflipPipeline":{config_parameters:[4,2,1,""],get_op_matrix:[4,2,1,""],need_data_info:[4,2,1,""],switch_points:[4,2,1,""]},"ida_lib.core.pipeline_local_ops":{BlurPipeline:[4,1,1,""],GaussianBlurPipeline:[4,1,1,""],GaussianNoisePipeline:[4,1,1,""],PoissonNoisePipeline:[4,1,1,""],SaltAndPepperNoisePipeline:[4,1,1,""],SpekleNoisePipeline:[4,1,1,""]},"ida_lib.core.pipeline_local_ops.BlurPipeline":{apply_to_image_if_probability:[4,2,1,""],get_op_matrix:[4,2,1,""]},"ida_lib.core.pipeline_local_ops.GaussianBlurPipeline":{apply_to_image_if_probability:[4,2,1,""],get_op_matrix:[4,2,1,""]},"ida_lib.core.pipeline_local_ops.GaussianNoisePipeline":{apply_to_image_if_probability:[4,2,1,""],get_op_matrix:[4,2,1,""]},"ida_lib.core.pipeline_local_ops.PoissonNoisePipeline":{apply_to_image_if_probability:[4,2,1,""],get_op_matrix:[4,2,1,""]},"ida_lib.core.pipeline_local_ops.SaltAndPepperNoisePipeline":{apply_to_image_if_probability:[4,2,1,""],get_op_matrix:[4,2,1,""]},"ida_lib.core.pipeline_local_ops.SpekleNoisePipeline":{apply_to_image_if_probability:[4,2,1,""],get_op_matrix:[4,2,1,""]},"ida_lib.core.pipeline_operations":{PipelineOperation:[4,1,1,""]},"ida_lib.core.pipeline_operations.PipelineOperation":{apply_according_to_probability:[4,2,1,""],get_op_matrix:[4,2,1,""],get_op_type:[4,2,1,""]},"ida_lib.core.pipeline_pixel_ops":{BrightnessPipeline:[4,1,1,""],ContrastPipeline:[4,1,1,""],DenormalizePipeline:[4,1,1,""],GammaPipeline:[4,1,1,""],NormalizePipeline:[4,1,1,""],RandomBrightnessPipeline:[4,1,1,""],RandomContrastPipeline:[4,1,1,""],RandomGammaPipeline:[4,1,1,""]},"ida_lib.core.pipeline_pixel_ops.BrightnessPipeline":{get_op_matrix:[4,2,1,""],get_op_type:[4,2,1,""],transform_function:[4,2,1,""]},"ida_lib.core.pipeline_pixel_ops.ContrastPipeline":{get_op_matrix:[4,2,1,""],transform_function:[4,2,1,""]},"ida_lib.core.pipeline_pixel_ops.DenormalizePipeline":{get_op_matrix:[4,2,1,""],transform_function:[4,2,1,""]},"ida_lib.core.pipeline_pixel_ops.GammaPipeline":{get_op_matrix:[4,2,1,""],transform_function:[4,2,1,""]},"ida_lib.core.pipeline_pixel_ops.NormalizePipeline":{get_op_matrix:[4,2,1,""],transform_function:[4,2,1,""]},"ida_lib.core.pipeline_pixel_ops.RandomBrightnessPipeline":{get_op_matrix:[4,2,1,""],get_op_type:[4,2,1,""],transform_function:[4,2,1,""]},"ida_lib.core.pipeline_pixel_ops.RandomContrastPipeline":{get_op_matrix:[4,2,1,""],transform_function:[4,2,1,""]},"ida_lib.core.pipeline_pixel_ops.RandomGammaPipeline":{get_op_matrix:[4,2,1,""],transform_function:[4,2,1,""]},"ida_lib.image_augmentation":{augment_to_disk:[5,0,0,"-"],data_loader:[5,0,0,"-"]},"ida_lib.image_augmentation.augment_to_disk":{AugmentToDisk:[5,1,1,""]},"ida_lib.image_augmentation.augment_to_disk.AugmentToDisk":{final_save:[5,2,1,""],save_item:[5,2,1,""]},"ida_lib.image_augmentation.data_loader":{AugmentDataLoader:[5,1,1,""]},"ida_lib.image_augmentation.data_loader.AugmentDataLoader":{InnerDataset:[5,1,1,""]},"ida_lib.operations":{geometry_ops_functional:[6,0,0,"-"],pixel_ops_functional:[6,0,0,"-"],transforms:[6,0,0,"-"],utils:[6,0,0,"-"]},"ida_lib.operations.geometry_ops_functional":{affine_compose_data:[6,3,1,""],affine_coordinates_matrix:[6,3,1,""],affine_image:[6,3,1,""],config_scale_matrix:[6,3,1,""],get_rotation_matrix:[6,3,1,""],get_scale_matrix:[6,3,1,""],get_shear_matrix:[6,3,1,""],get_squared_scale_matrix:[6,3,1,""],get_squared_shear_matrix:[6,3,1,""],get_translation_matrix:[6,3,1,""],hflip_compose_data:[6,3,1,""],hflip_coordinates_matrix:[6,3,1,""],hflip_image:[6,3,1,""],own_affine:[6,3,1,""],prepare_data:[6,3,1,""],rotate_compose_data:[6,3,1,""],rotate_coordinates_matrix:[6,3,1,""],rotate_image:[6,3,1,""],scale_compose_data:[6,3,1,""],scale_coordinates_matrix:[6,3,1,""],scale_image:[6,3,1,""],shear_compose_data:[6,3,1,""],shear_coordinates_matrix:[6,3,1,""],shear_image:[6,3,1,""],translate_compose_data:[6,3,1,""],translate_coordinates_matrix:[6,3,1,""],translate_image:[6,3,1,""],vflip_compose_data:[6,3,1,""],vflip_coordinates_matrix:[6,3,1,""],vflip_image:[6,3,1,""]},"ida_lib.operations.pixel_ops_functional":{apply_blur:[6,3,1,""],apply_gaussian_blur:[6,3,1,""],apply_gaussian_noise:[6,3,1,""],apply_lut_by_pixel_function:[6,3,1,""],apply_poisson_noise:[6,3,1,""],apply_salt_and_pepper_noise:[6,3,1,""],apply_spekle_noise:[6,3,1,""],blur:[6,3,1,""],change_brightness:[6,3,1,""],change_contrast:[6,3,1,""],change_gamma:[6,3,1,""],gaussian_blur:[6,3,1,""],gaussian_noise:[6,3,1,""],get_brightness_function:[6,3,1,""],get_contrast_function:[6,3,1,""],get_gamma_function:[6,3,1,""],histogram_equalization:[6,3,1,""],normalize_image:[6,3,1,""],poisson_noise:[6,3,1,""],prepare_data_for_opencv:[6,3,1,""],salt_and_pepper_noise:[6,3,1,""],spekle_noise:[6,3,1,""]},"ida_lib.operations.transforms":{affine:[6,3,1,""],blur:[6,3,1,""],change_brightness:[6,3,1,""],change_contrast:[6,3,1,""],change_gamma:[6,3,1,""],equalize_histogram:[6,3,1,""],gaussian_blur:[6,3,1,""],hflip:[6,3,1,""],inject_gaussian_noise:[6,3,1,""],inject_poisson_noise:[6,3,1,""],inject_salt_and_pepper_noise:[6,3,1,""],inject_spekle_noise:[6,3,1,""],rotate:[6,3,1,""],scale:[6,3,1,""],shear:[6,3,1,""],translate:[6,3,1,""],vflip:[6,3,1,""]},"ida_lib.operations.utils":{add_new_axis:[6,3,1,""],arrays_equal:[6,3,1,""],data_to_numpy:[6,3,1,""],dtype_to_torch_type:[6,3,1,""],element_to_dict_csv_format:[6,3,1,""],get_principal_type:[6,3,1,""],get_torch_image_center:[6,3,1,""],homogeneous_points_to_list:[6,3,1,""],homogeneous_points_to_matrix:[6,3,1,""],is_a_normalized_image:[6,3,1,""],is_numpy_data:[6,3,1,""],keypoints_to_homogeneous_and_concatenate:[6,3,1,""],keypoints_to_homogeneous_functional:[6,3,1,""],map_value:[6,3,1,""],mask_change_to_01_functional:[6,3,1,""],remove_digits:[6,3,1,""],round_torch:[6,3,1,""],save_im:[6,3,1,""]},"ida_lib.visualization":{plot_image_transformation:[3,3,1,""],visualize:[3,3,1,""]},ida_lib:{core:[4,0,0,"-"],image_augmentation:[5,0,0,"-"],operations:[6,0,0,"-"],visualization:[3,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","function","Python function"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:function"},terms:{"1x2":10,"2x3":6,"abstract":4,"byte":1,"case":5,"class":[0,1,4,5],"default":[5,6],"final":9,"float":[0,1,4,6],"function":[1,4,6,7,11],"import":[0,1,9,10],"int":[3,4,5,6],"jos\u00e9":7,"mar\u00eda":7,"new":[4,9],"nicol\u00e1":7,"return":[0,1,4,6],"static":4,"true":[1,4,5,6,10],"try":9,"var":[4,6],For:[6,9,10],IDE:7,Its:10,That:5,The:[4,5,6,7,9,11],Useful:5,__getitem__:[0,1],__init__:[0,1],__len__:[0,1],_variablefunct:[4,6],abc:4,about:4,accept:4,accord:[4,5],activ:[4,6,11],adapt:1,add:[4,5],add_new_axi:6,adding:[4,11],adjust:[6,11],affect:[4,6],affin:[6,11],affine_compose_data:6,affine_coordinates_matrix:6,affine_imag:6,align:[],all:[0,1,2,5,6,9],allow:[4,5,7,9],also:9,alter:6,amount:[4,6,11],analyz:4,ani:[4,9],annot:[0,1,5],anot:0,anoth:4,apertur:[4,11],api:7,appli:[0,4,5,6,9,11],apply_according_to_prob:4,apply_blur:6,apply_gaussian_blur:6,apply_gaussian_nois:6,apply_lut_by_pixel_funct:6,apply_poisson_nois:6,apply_salt_and_pepper_nois:6,apply_spekle_nois:6,apply_to_image_if_prob:4,arg:[0,1],arr1:6,arr2:6,arr:6,arrai:[0,1,10],arrang:5,arrays_equ:6,associ:[5,7,9],astyp:[0,1,10],attribut:9,augment:[1,2,5,6,7,9],augment_to_disk:[0,3],augmentdataload:[1,5],augmented_custom:0,augmentor:0,augmenttodisk:[0,5],author:7,auxiliar:1,axi:[6,11],base:[4,5,7],batch:[3,4,9,10],batch_info:4,batch_siz:[1,5],becaus:[0,1],been:[1,5],befor:[3,4,7],beginn:1,being:4,better:7,bgr:10,bilinear:[1,4,5,6],bin:10,bit:[1,10],black:[4,6,11],blanco:7,blob:9,block:[],blur:[4,6,11],blur_siz:[4,6],blurpipelin:4,bodi:[],bokeh:[3,7,9],bool:[4,6],border:6,boundari:10,bpp:4,bright:[4,6,11],brightness_factor:4,brightness_rang:4,brightnesspipelin:4,calcul:[4,6],callabl:0,can:[2,4,5,7,9,10],care:5,carreira:7,carri:[6,11],cell:[],center:[4,6],center_devi:[0,4],central:9,chang:[4,6,11],change_bright:6,change_contrast:6,change_gamma:6,citiu:7,classic:9,close:9,code:[1,7,9],coher:[4,11],color:[4,6,9],color_bgr2rgb:10,column:5,com:[2,7,9],combin:[4,7,9],compani:7,compar:9,complet:[7,9],compos:[4,9,11],composit:9,comput:7,concaten:6,config_paramet:4,config_scale_matrix:6,configur:4,consider:4,consum:10,consumed_tim:10,contain:[6,10],content:3,contrast:[4,6,11],contrast_factor:[1,4],contrast_pipelin:4,contrast_rang:[0,4],contrastpipelin:[1,4],convers:4,convert:7,coordin:[4,5,6,10],copi:10,core:[0,1,3,7,10],correct:[6,11],correctli:[4,9],correspond:[4,5,6],counterclockwis:[6,11],cpu:1,creat:[0,1,10],crop:11,csv:[0,1,5],csv_file:[0,1],custom:[0,1,5],cv2:[6,10],cvtcolor:10,data1:9,data2:9,data3:9,data:[0,1,3,4,5,6,7,9,10],data_info:4,data_load:[1,3],data_loading_tutori:1,data_origin:[3,4],data_to_numpi:6,data_typ:[5,10],dataaugmentdataload:5,dataload:[2,5,7,9],dataset:[0,1,5,9],datset:0,debug:[6,9],decid:9,declar:10,decor:6,dedic:7,def:[0,1],defin:[9,10],degrad:[4,11],degre:[4,6,9,11],degrees_rang:[4,9,10],denorm:4,denormalizepipelin:4,densiti:[4,11],deploi:[8,9],desir:[4,6],develop:[7,9],dict:[3,4,5,6,9],dictionari:[5,6],differ:[0,4,9,10],differenti:9,dimens:10,dimension:[5,6],direct:11,directli:[5,9],directori:[0,1,5],discret:4,disk:[2,5,7,9],displac:11,displai:[1,6,9,10],distanc:11,distribut:[4,6,11],divers:7,divid:9,document:10,doe:9,don:10,dont:6,dot:9,dtype:[4,5,6,10],dtype_to_torch_typ:6,each:[4,5,6,9,10,11],effici:[7,9],element:[1,3,4,5,6,9,10],element_to_dict_csv_format:6,enter:4,entir:1,entri:9,enumer:1,epoch:1,equal:[4,6,11],equalize_histogram:6,equival:[6,11],everi:4,exactli:9,exampl:[4,7,9],example_pipipelin:9,exchange_point:[4,9,10],execut:[4,9,10],exist:[4,11],express:[10,11],extens:5,face:[0,1],face_dataset:[0,1],face_landmark:[0,1],facelandmarksdataset:[0,1],facilit:9,factor:[4,6],fals:[4,6,10],fast:7,file:[0,1,5,10],final_sav:5,find:2,first:7,firstli:1,fix:11,flexibl:7,flip:[4,6,11],float32:10,focus:9,follow:[1,5],form:[4,5],format:[4,10],framework:[7,9],from:[0,1,7,10,11],func:6,futur:[5,9],gamma:[4,6,11],gamma_factor:4,gamma_rang:4,gammapipelin:4,gaussian:[4,6,11],gaussian_blur:6,gaussian_nois:6,gaussianblurpipelin:4,gaussiannoisepipelin:[4,10],gener:[3,4,5,9,10],geometr:[4,6],geometri:4,geometry_ops_funct:3,get:7,get_brightness_funct:6,get_compose_funct:4,get_compose_matrix:4,get_contrast_funct:6,get_data_typ:4,get_gamma_funct:6,get_op_matrix:4,get_op_typ:4,get_principal_typ:6,get_rotation_matrix:6,get_scale_matrix:6,get_shear_matrix:6,get_squared_scale_matrix:6,get_squared_shear_matrix:6,get_torch_image_cent:6,get_translation_matrix:6,git:7,github:[2,7,9],give:4,goe:11,going:10,good:10,gpu:4,granular:[4,11],grid:6,group:[5,6,9],has:1,have:[0,1,4,5,9,11],header:[],heat:7,heatmap:[9,10],heatmap_complet:10,height:6,here:[0,2],hflip:[6,11],hflip_compose_data:6,hflip_coordinates_matrix:6,hflip_imag:6,hflip_pipelin:4,hflippipelin:[0,1,4,9,10],histogram2d:10,histogram:[6,11],histogram_equ:6,homogen:[4,6],homogeneous_points_to_list:6,homogeneous_points_to_matrix:6,horizont:[4,6,11],how:[1,10],html:1,http:[1,2,7,9],i_batch:1,id_imag:5,ida:[1,7,9],ida_lib:[0,1,2,7,9,10],idalib:[1,9,10],ident:10,identifi:[4,5,9],idx:[0,1],iloc:[0,1],im_typ:6,imag:[1,2,3,4,5,6,7,9,10,11],image1:9,image2:9,image_augment:[0,1,3,7],images_origin:3,img1:9,img2:9,img3:9,img:[1,4,6,10,11],img_nam:[0,1],implement:[4,5],importantto:10,imput:0,imread:[0,1,10],imshow:1,in_max:6,in_min:6,includ:[1,4,7,9,11],increas:[6,9],independ:4,index:[5,7],indic:[1,4,6,9,11],info:4,inform:[4,10],inher:[4,11],inici:0,initi:[0,1],initialit:1,inject:[6,11],inject_gaussian_nois:6,inject_poisson_nois:6,inject_salt_and_pepper_nois:6,inject_spekle_nois:6,inner:5,innerdataset:5,input:[0,1,3,4,5,6,7,10],input_list:4,integr:9,interact:9,interest:5,interfer:[4,11],intern:5,interpol:[0,1,4,5,6,10],is_a_normalized_imag:6,is_numpy_data:6,is_tensor:[0,1],item:[0,3,5,6,10],item_id:0,iter:5,its:[4,5,6,9,10,11],join:[0,1],joint:[4,9],jpg:[0,5,10],just:[9,10],keep:10,keep_aspect:4,keypoint:[1,4,6,7,9,10],keypoints2:9,keypoints3:9,keypoints_to_homogeneous_and_concaten:6,keypoints_to_homogeneous_funct:6,kornia:[1,7],label:[5,6],lambda:6,landmark:[0,1],landmarks_fram:[0,1],larger:[7,11],last:4,latest:7,learn:7,len:[0,1],level:9,lib:[1,7,9],librari:[7,11],like:[1,10],limit:10,line:11,linear:11,list:[3,4,5,10],load:4,lumin:[4,6,11],lut:[4,6],machin:7,mai:[],make:[5,10,11],mani:9,map:[6,7,10,11],map_valu:6,marker:1,mask1:[9,10],mask2:10,mask67:9,mask:[4,6,7,9,10],mask_change_to_01_funct:6,mask_example1:[9,10],mask_example2:[9,10],mask_example3:9,master:[2,9],mathemat:6,matplotlib:1,matrix:[4,6,11],matrix_coordin:6,matrix_transform:6,max:[3,6],max_imag:3,mean:[4,6],measur:10,medic:[4,11],metadata:4,method:5,micki:10,min:10,mind:10,mode:[4,6],modif:6,modifi:6,modul:7,more:[7,10],move:11,multipl:[4,6,7],multipli:[4,11],must:[1,4,9],n_digit:6,name:[4,5,6,10],ndarrai:[4,6,10],nearest:[0,6,10],necessari:[0,4,5,9],need_data_info:4,network:[4,5,7,9],neural:[4,5,7,9],new_rang:4,nois:[4,6,11],non:4,none:[0,4,5,6],norm_ham:6,norm_hamming2:6,norm_inf:6,norm_minmax:6,norm_rel:6,norm_typ:6,normal:[1,4,6,11],normalize_imag:6,normalizepipelin:4,nouch:7,number:[0,1,3,5,6,9,10],number_of_iter:1,number_of_point:10,numpi:[0,1,4,6,10],nx2:10,object:[3,4,5,9],obtain:9,occupi:6,offer:9,old_rang:4,onc:[5,9],one:[5,6,7,9,10],onli:[5,6,9],op_typ:4,open:9,opencv:[6,7,10],oper:[0,3,4,5,7,9,10,11],optic:[4,11],option:[0,4,5,6,9],order:[4,9],org:[1,7],organ:5,origin:[1,3,4,6,11],original_typ:4,other:[3,4,5,9],other_typ:5,our:1,out:[6,11],out_max:6,out_min:6,output:[4,6],output_csv_path:[0,5],output_extens:[0,5],output_format:[4,5],output_path:[0,5],output_typ:[4,5],outsid:[6,10],over:[5,6,10],overhead:10,overview:7,overwritten:5,own:1,own_affin:6,packag:7,pad:6,padding_mod:[0,1,4,5,6],page:7,panda:[0,1],parallel:11,param:6,paramet:[0,3,4,5,6,9],parameteriz:9,particular:4,pass:[9,10],path:[0,1,5],paus:1,pdf:[4,11],pepper:[4,6,11],per:[0,10],percentag:6,perform:[1,5,6,7,9,10],person:5,pictur:4,pip:[4,7,10],pipe:4,pipelin:[1,3,5,7,9],pipeline_funct:3,pipeline_geometric_op:[0,1,3,10],pipeline_local_op:[3,10],pipeline_oper:[1,3,5,9,10],pipeline_pixel_op:[0,1,3],pipeline_usag:9,pipelineoper:[4,9],pixel:[4,6,10,11],pixel_ops_funct:3,place:4,plot:[1,3],plot_image_transform:3,plt:1,png:[],point0_i:5,point0_x:5,point1_x:5,point:[4,5,6,11],point_i:5,point_matrix:4,poison:4,poisson:[4,6,11],poisson_nois:6,poissonnoisepipelin:4,posit:11,possibl:[4,9],postprocess_data:4,prepar:[4,6],prepare_data:6,prepare_data_for_opencv:6,preprocess:4,preprocess_data:4,previou:9,print:[1,10],probabl:[0,1,4,9,10,11],process:[1,4,5,6,10],program:9,project:7,proport:11,provid:[0,5],purpos:6,pycharm:7,pypi:7,pyplot:1,python:9,pytorch:[1,5,7],qualiti:[4,11],radar:[4,11],randint:10,randn:10,random:[4,9,10],random_brightness_pipelin:4,random_coordin:[9,10],random_coordinates2:9,random_coordinates3:9,random_rotate_pipelin:4,random_scale_pipelin:4,randombrightnesspipelin:4,randomcontrastpipelin:[0,4],randomgammapipelin:4,randomrotatepipelin:[4,9,10],randomscalepipelin:[0,4],randomshearpipelin:[1,4],randomtranslatepipelin:4,rang:[1,4,9,10],raquelvilas18:[2,7,9],read:[0,1,5,10],read_csv:[0,1],reflect:6,releas:7,remain:6,rememb:9,remov:6,remove_digit:6,repeat:10,repres:[4,6],requir:4,reshap:[0,1,10],resiz:[0,1,4,5],resize_factor:6,respect:6,restor:4,result:10,rgb:10,rome:7,rometool:7,root_dir:[0,1],rotat:[4,6,11],rotate_compose_data:6,rotate_coordinates_matrix:6,rotate_imag:6,rotatepipelin:[4,9],round_torch:6,row:5,run:[0,4,5,9],s_vs_p:[4,6],salt:[4,6,11],salt_and_pepper_nois:6,saltandpeppernoisepipelin:4,same:[1,4,5,6,10],same_translation_on_axi:4,sampl:[0,1,5,10],sample_batch:1,samples_per_item:[0,5],sar:[4,11],save:5,save_im:6,save_item:5,scale:[4,6,11],scale_compose_data:6,scale_coordinates_matrix:6,scale_factor:[4,6,9,10],scale_imag:6,scale_rang:[0,4],scalepipelin:[4,9,10],scatter:1,search:7,see:[9,10],segmap:[4,9,10],segment:[7,10],select:9,self:[0,1],separ:[4,5],serv:5,server:9,set:[0,10],shape:[4,10],shear:[4,6,9,10,11],shear_compose_data:6,shear_coordinates_matrix:6,shear_factor:6,shear_imag:6,shear_rang:[1,4],shearpipelin:[4,9,10],short_siz:10,show:1,show_landmark:1,shown:[3,10],shuffl:[1,5],sign:11,signific:10,simpl:7,singl:[4,6],situat:9,size:[0,1,4],skimag:[0,1],smaller:[6,11],span:[],special:4,specifi:5,speckl:[4,11],spekl:[4,11],spekle_nois:6,speklenoisepipelin:4,split:[0,4],split_operations_by_typ:4,start_tim:10,statist:[4,11],step:7,store:5,str:[4,5,6,10],string:[0,1],sub:4,submodul:7,suppli:9,support:7,sure:10,surround:6,switch_point:4,switch_point_posit:4,synthet:[4,11],system:5,tab:3,tabl:4,tag:4,take:[5,9,10],taken:6,target:[4,9],task:7,tensor:[4,6],tensor_to_imag:1,test:9,than:[6,10],thei:[6,10],them:[4,9,10],therefor:9,thi:[1,4,5,6,7,9,10],those:6,through:[4,9,10,11],time:[1,9,10],titl:6,tolist:[0,1],tomographi:[4,11],tool:[4,6,7],torch:[0,1,4,5,6],total:[6,10],total_output_sampl:5,train:7,transform:[0,3,4,7,9,10],transform_funct:4,transformed_batch:9,translat:[1,4,6,9,10,11],translate_compose_data:6,translate_coordinates_matrix:6,translate_imag:6,translate_pipelin:4,translatepipelin:[1,4,9,10],translation_rang:4,treat:9,treatment:4,tree:2,tupl:[4,5,6],tutori:1,two:[5,6],type:[4,5,6,7,9,10],types_2d:5,uint8:[4,10],ultrasound:[4,11],unchang:6,understand:10,uniform_nois:[4,11],union:[4,6],updat:1,usag:7,use:[1,5,7,9,10],used:[5,7,9,10],user:5,uses:5,using:[1,6],util:[0,3,5],valu:[4,6,9],varianc:6,varieti:9,veri:10,version:7,vertic:[4,6,11],vflip:[6,11],vflip_compose_data:6,vflip_coordinates_matrix:6,vflip_imag:6,vflip_pipelin:4,vflippipelin:[1,4],view:9,vila:7,vision:7,visual:[4,6,7,10],wai:[5,7],want:[4,7,9],warp:6,weight:4,what:9,when:[4,5],where:9,whether:4,which:[1,5,6,9,10],white:[4,6,11],wide:9,width:6,window:9,within:[4,9],work:[1,10],write:5,written:5,xedg:10,yedg:10,you:[2,7,9,10],your:[1,5,7,9],zero:[0,1,4,5,6,10]},titles:["Image Augmentation to Disk example","Dataloader Usage example","Examples","API","ida_lib.core package","ida_lib.image_augmentation package","ida_lib.operations package","IdaLib","Pipeline Usage example","Overview","Pipeline Usage example","Transformations"],titleterms:{"function":9,acknowledg:7,api:3,augment:0,augment_to_disk:5,built:7,content:[4,5,6,7],core:4,data_load:5,dataload:1,disk:0,exampl:[0,1,2,8,10],featur:7,first:9,geometry_ops_funct:6,ida_lib:[3,4,5,6],idalib:7,imag:0,image_augment:5,indic:7,instal:7,modul:[3,4,5,6],oper:6,overview:9,packag:[3,4,5,6],pipelin:[2,4,8,10],pipeline_funct:4,pipeline_geometric_op:4,pipeline_local_op:4,pipeline_oper:4,pipeline_pixel_op:4,pixel_ops_funct:6,step:9,submodul:[3,4,5,6],tabl:7,tool:9,transform:[6,11],usag:[1,2,8,10],util:6,visual:[3,9]}})