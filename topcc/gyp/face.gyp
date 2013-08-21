{
  'variables': {
   'ICE_PATH':'/opt/Ice-3.3.1',#'<!(echo $ICE_HOME)',
   'FACE_ROOT':'../FaceInterfaces',
   'FACE_LANDMARK':'../FaceInterfaces/facelandmark',
   'FACE_ACTION':'../face_new',
   'FACE_CLUSTER':'../face_cluster',
   'FACE_STORE':'../face_store',
   'SLICE2CPP_PATH':'<(ICE_PATH)/bin/slice2cpp',
  },
 'conditions':[
    ['OS=="linux"', {
     'target_defaults': {
       'cflags':['-fPIC', '-g'],
       'defines':['OS_LINUX', 'POSIX',
       'NDEBUG'],
       'include_dirs':[
         '..',
         '<(ICE_PATH)/include',
         ],
        },
      },
    ],
    ['OS=="win"', {'target_defaults': {},},],
  ],
  'targets': [
   { 'target_name': 'facelandmark',
   'type': 'static_library',
   'include_dirs':[
   '/usr/local/include/gsl',
   ],
   'conditions':[
      ['OS=="linux"', 
      {
       'cflags':['-O3'],
       'defines':['HAVE_CONFIG_H','STDC_HEADERS','REGEX_MALLOC'],
      }
      ],
   ],
   'sources': [
'<(FACE_LANDMARK)/asmsearch.cpp',
'<(FACE_LANDMARK)/asmsearch.hpp',
'<(FACE_LANDMARK)/atface.cpp',
'<(FACE_LANDMARK)/atface.hpp',
'<(FACE_LANDMARK)/colors.hpp',
'<(FACE_LANDMARK)/err.cpp',
'<(FACE_LANDMARK)/err.hpp',
'<(FACE_LANDMARK)/eyesynth.hpp',
'<(FACE_LANDMARK)/ezfont.c',
'<(FACE_LANDMARK)/ezfont.h',
'<(FACE_LANDMARK)/facelandmark.cpp',
'<(FACE_LANDMARK)/facelandmark.h',
'<(FACE_LANDMARK)/find.cpp',
'<(FACE_LANDMARK)/find.hpp',
'<(FACE_LANDMARK)/follow.cpp',
'<(FACE_LANDMARK)/follow.hpp',
'<(FACE_LANDMARK)/forward.cpp',
'<(FACE_LANDMARK)/forward.hpp',
'<(FACE_LANDMARK)/image.hpp',
'<(FACE_LANDMARK)/imfile.cpp',
'<(FACE_LANDMARK)/imfile.hpp',
'<(FACE_LANDMARK)/imgiven.hpp',
'<(FACE_LANDMARK)/imshape.cpp',
'<(FACE_LANDMARK)/imshape.hpp',
'<(FACE_LANDMARK)/imutil.cpp',
'<(FACE_LANDMARK)/imutil.hpp',
'<(FACE_LANDMARK)/imwrite.cpp',
'<(FACE_LANDMARK)/imwrite.hpp',
'<(FACE_LANDMARK)/initasm.cpp',
'<(FACE_LANDMARK)/initasm.hpp',
'<(FACE_LANDMARK)/initnet.cpp',
'<(FACE_LANDMARK)/initnet.hpp',
'<(FACE_LANDMARK)/jpegutil.hpp',
'<(FACE_LANDMARK)/landmarks.cpp',
'<(FACE_LANDMARK)/landmarks.hpp',
'<(FACE_LANDMARK)/list.cpp',
'<(FACE_LANDMARK)/list.hpp',
'<(FACE_LANDMARK)/mat.cpp',
'<(FACE_LANDMARK)/mat.hpp',
'<(FACE_LANDMARK)/matvec.cpp',
'<(FACE_LANDMARK)/matvec.hpp',
'<(FACE_LANDMARK)/matview.hpp',
'<(FACE_LANDMARK)/mchol.cpp',
'<(FACE_LANDMARK)/mchol.hpp',
'<(FACE_LANDMARK)/me17s.hpp',
'<(FACE_LANDMARK)/mouth.hpp',
'<(FACE_LANDMARK)/mrand.cpp',
'<(FACE_LANDMARK)/mrand.hpp',
'<(FACE_LANDMARK)/path.txt',
'<(FACE_LANDMARK)/pngutil.hpp',
'<(FACE_LANDMARK)/prof.cpp',
'<(FACE_LANDMARK)/prof.hpp',
'<(FACE_LANDMARK)/proftrain.hpp',
'<(FACE_LANDMARK)/readasm.cpp',
'<(FACE_LANDMARK)/readasm.hpp',
'<(FACE_LANDMARK)/readconf.cpp',
'<(FACE_LANDMARK)/readconf.hpp',
'<(FACE_LANDMARK)/regex.c',
'<(FACE_LANDMARK)/regex_config.h',
'<(FACE_LANDMARK)/regex.h',
'<(FACE_LANDMARK)/release.cpp',
'<(FACE_LANDMARK)/release.hpp',
'<(FACE_LANDMARK)/rgbimutil.cpp',
'<(FACE_LANDMARK)/rgbimutil.hpp',
'<(FACE_LANDMARK)/rowley.cpp',
'<(FACE_LANDMARK)/rowleyhand.cpp',
'<(FACE_LANDMARK)/rowleyhand.hpp',
'<(FACE_LANDMARK)/rowley.hpp',
'<(FACE_LANDMARK)/safe_alloc.cpp',
'<(FACE_LANDMARK)/safe_alloc.hpp',
'<(FACE_LANDMARK)/search.cpp',
'<(FACE_LANDMARK)/search.hpp',
'<(FACE_LANDMARK)/shapefile.cpp',
'<(FACE_LANDMARK)/shapefile.hpp',
'<(FACE_LANDMARK)/shapemodel.cpp',
'<(FACE_LANDMARK)/shapemodel.hpp',
'<(FACE_LANDMARK)/sparsemat.cpp',
'<(FACE_LANDMARK)/sparsemat.hpp',
'<(FACE_LANDMARK)/startshape.cpp',
'<(FACE_LANDMARK)/startshape.hpp',
'<(FACE_LANDMARK)/stasm.hpp',
'<(FACE_LANDMARK)/tab.hpp',
'<(FACE_LANDMARK)/tasm.hpp',
'<(FACE_LANDMARK)/tclHash.c',
'<(FACE_LANDMARK)/tclHash.h',
'<(FACE_LANDMARK)/tcovar.hpp',
'<(FACE_LANDMARK)/tree.txt',
'<(FACE_LANDMARK)/util.cpp',
'<(FACE_LANDMARK)/util.hpp',
'<(FACE_LANDMARK)/violajones.hpp',
'<(FACE_LANDMARK)/vjhand.cpp',
'<(FACE_LANDMARK)/vjhand.hpp',
    ],
   },

   { 'target_name': 'interface_test',
   'type': 'executable',
   'include_dirs':[
     '../FaceInterfaces',
    '/usr/local/include/opencv',
   ],
   'conditions':[
      ['OS=="linux"', {
        'libraries': ['-lboost_system',
                      #'-lboost_thread',
                      '-lgslcblas','-lgsl','-lfacelandmark',
                      '-lopencv_core','-lopencv_objdetect','-lopencv_highgui','-lopencv_imgproc',
                      ],

        'link_settings': {
          'ldflags': [
           '-Wl,-rpath /usr/local/lib',
          ],
        },
     }],
   ],
   'sources': [
      '<(FACE_ROOT)/faceclassifier/faceclassifier.h',
      '<(FACE_ROOT)/faceclassifier/faceclassifierimpl.h',
      '<(FACE_ROOT)/faceclassifier/faceclassifierimpl.cpp',
      '<(FACE_ROOT)/faceclustering/cluster.cpp',
      '<(FACE_ROOT)/faceclustering/cluster.h',
      '<(FACE_ROOT)/faceclustering/faceclustering.h',
      '<(FACE_ROOT)/faceclustering/faceclusteringimpl.h',
      '<(FACE_ROOT)/faceclustering/faceclusteringimpl.cpp',
      '<(FACE_ROOT)/faceclustering/faceclusters.cpp',
      '<(FACE_ROOT)/faceclustering/faceclusters.h',
      '<(FACE_ROOT)/facedetection/facedetector.h',
      '<(FACE_ROOT)/facedetection/facedetectorimpl.h',
      '<(FACE_ROOT)/facedetection/facedetectorimpl.cpp',
      '<(FACE_ROOT)/facefeature/elasticmatch.cpp',
      '<(FACE_ROOT)/facefeature/facefeature.h',
      '<(FACE_ROOT)/facefeature/facefeatureimpl.h',
      '<(FACE_ROOT)/facefeature/facefeatureimpl.cpp',
      '<(FACE_ROOT)/facefeature/facelandmark.h',
      '<(FACE_ROOT)/facefeature/HOG.cpp',
      '<(FACE_ROOT)/facefeature/LBP.cpp',
      '<(FACE_ROOT)/facerecognize/faceclassifier.h',
      '<(FACE_ROOT)/facerecognize/facerecognize.cpp',
      '<(FACE_ROOT)/facerecognize/intkey.cpp',
      '<(FACE_ROOT)/facerecognize/intkey.h',
      '<(FACE_ROOT)/include/facerecognize.h',
      '<(FACE_ROOT)/include/faceutils.h',
      '<(FACE_ROOT)/include/public.h',
      '<(FACE_ROOT)/InterfaceTest.cpp',
      '<(FACE_ROOT)/ptime.h',
    ],
   },

   { 'target_name': 'facefeature.fcgi',
   'type': 'executable',
   'include_dirs':[
     '../cwf/src',
     '../FaceInterfaces',
    '/usr/local/include/opencv',
#    '/root/tair_bin/include',
#    '/usr/local/lib/include/tbnet',
#    '/usr/local/lib/include/tbsys',
   ],
   'dependencies':[
      '../cwf/gyp/base3.gyp:base3',
      'jsoncpp.gyp:json',
      '../cwf/gyp/cwf.gyp:cwf',
      '../cwf/gyp/cwf.gyp:cwfmain',
      'ice.gyp:utiladapter',
      'ice.gyp:oceadapter',
#      'dbdesc.gyp:dbpool',
   ],
   'export_dependent_settings': ['jsoncpp.gyp:json'],
   'conditions':[
      ['OS=="linux"', {
        'libraries': ['-lboost_system',
                      '-lboost_thread',
                      '-lssl' , '-lmemcached', 
                      '-lgslcblas','-lgsl','-lfacelandmark',
                      '-lopencv_core','-lopencv_objdetect','-lopencv_highgui','-lopencv_imgproc',
#                      '-ltairclientapi','-ltbsys','-ltbnet',
#                      '-L/root/tair_bin/lib/',
                      ],

        'link_settings': {
          'ldflags': [
           '-Wl,-rpath /usr/local/lib',
           #'-Wl,-rpath <(ICE_PATH)/lib64'
          ],
        },
     }],
   ],
   'sources': [
      '<(FACE_ROOT)/faceclassifier/faceclassifier.h',
      '<(FACE_ROOT)/faceclassifier/faceclassifierimpl.h',
      '<(FACE_ROOT)/faceclassifier/faceclassifierimpl.cpp',
      '<(FACE_ROOT)/faceclustering/cluster.cpp',
      '<(FACE_ROOT)/faceclustering/cluster.h',
      '<(FACE_ROOT)/faceclustering/faceclustering.h',
      '<(FACE_ROOT)/faceclustering/faceclusteringimpl.h',
      '<(FACE_ROOT)/faceclustering/faceclusteringimpl.cpp',
      '<(FACE_ROOT)/faceclustering/faceclusters.cpp',
      '<(FACE_ROOT)/faceclustering/faceclusters.h',
      '<(FACE_ROOT)/facedetection/facedetector.h',
      '<(FACE_ROOT)/facedetection/facedetectorimpl.h',
      '<(FACE_ROOT)/facedetection/facedetectorimpl.cpp',
      '<(FACE_ROOT)/facefeature/elasticmatch.cpp',
      '<(FACE_ROOT)/facefeature/facefeature.h',
      '<(FACE_ROOT)/facefeature/facefeatureimpl.h',
      '<(FACE_ROOT)/facefeature/facefeatureimpl.cpp',
      '<(FACE_ROOT)/facefeature/facelandmark.h',
      '<(FACE_ROOT)/facefeature/HOG.cpp',
      '<(FACE_ROOT)/facefeature/LBP.cpp',
      '<(FACE_ROOT)/facerecognize/faceclassifier.h',
      '<(FACE_ROOT)/facerecognize/facerecognize.cpp',
      '<(FACE_ROOT)/facerecognize/intkey.cpp',
      '<(FACE_ROOT)/facerecognize/intkey.h',
      '<(FACE_ROOT)/include/facerecognize.h',
      '<(FACE_ROOT)/include/faceutils.h',
      '<(FACE_ROOT)/include/public.h',
      '<(FACE_ACTION)/action_detect.h',
      '<(FACE_ACTION)/action_detect.cc',
      '<(FACE_ACTION)/memcache.h',
      '<(FACE_ACTION)/memcache.cpp',
      '<(FACE_ACTION)/registry.cc',
      '../arch_diff/IdCacheReaderAdapter.h',
      '../arch_diff/IdCacheReaderAdapter.cpp',
      '../arch_diff/BuddyByIdReplicaAdapter.h',
      '../arch_diff/BuddyByIdReplicaAdapter.cpp',
      '../arch_diff/BuddyCheckHelper.h',
      '../arch_diff/IpAddr.hpp',
      '../arch_diff/Markable.hpp',
      '../arch_diff/Date.h',
      '../arch_diff/Channel.h',
      '../arch_diff/Channel.cpp',
      '../arch_diff/TaskManager.h',
      '../arch_diff/TaskManager.cpp',
      '../arch_diff/ThreadPoolExecutor.cpp',
      '../arch_diff/ThreadPoolScheduler.cpp',
      '../arch_diff/ClientInterface.h',
      '../arch_diff/ClusterClient.h',
      '../arch_diff/ClusterStateSubscriber.h',
      '../arch_diff/ClusterStateSubscriber.cpp',
      '../arch_diff/Singleton.h',
      '../arch_diff/SbjTopicI.h',
      '../arch_diff/SbjTopicI.cpp',
      '../arch_diff/AdapterI.cpp',
      '../arch_diff/AdapterI.h',
      '../arch_diff/site_xiaonei.h',
      '../arch_diff/site_xiaonei.cc',
    ],
   },
{ 'target_name': 'facecluster.fcgi',
   'type': 'executable',
   'include_dirs':[
     '../cwf/src',
     '../FaceInterfaces',
    '/usr/local/include/opencv',
#    '/root/tair_bin/include',
#    '/usr/local/include/tbnet',
#    '/usr/local/include/tbsys',
   ],
   'dependencies':[
      '../cwf/gyp/base3.gyp:base3',
      'jsoncpp.gyp:json',
      '../cwf/gyp/cwf.gyp:cwf',
      '../cwf/gyp/cwf.gyp:cwfmain',
      'ice.gyp:utiladapter',
      'ice.gyp:oceadapter',
#      'dbdesc.gyp:dbpool',
   ],
   'export_dependent_settings': ['jsoncpp.gyp:json'],
   'conditions':[
      ['OS=="linux"', {
        'libraries': ['-lboost_system',
                      '-lboost_thread',
                      '-lssl' , '-lmemcached', 
                      '-lgslcblas','-lgsl',
                      '-lfacelandmark',
                      '-lopencv_core','-lopencv_objdetect','-lopencv_highgui','-lopencv_imgproc',
#                      '-ltairclientapi','-ltbsys','-ltbnet',
#                      '-L/root/tair_bin/lib/',
                      ],

        'link_settings': {
          'ldflags': [
           '-Wl,-rpath /usr/local/lib',
           '-Wl,-rpath <(ICE_PATH)/lib64'
          ],
        },
     }],
   ],
   'sources': [
      '<(FACE_ROOT)/faceclassifier/faceclassifier.h',
      '<(FACE_ROOT)/faceclassifier/faceclassifierimpl.h',
      '<(FACE_ROOT)/faceclassifier/faceclassifierimpl.cpp',
      '<(FACE_ROOT)/faceclustering/cluster.cpp',
      '<(FACE_ROOT)/faceclustering/cluster.h',
      '<(FACE_ROOT)/faceclustering/faceclustering.h',
      '<(FACE_ROOT)/faceclustering/faceclusteringimpl.h',
      '<(FACE_ROOT)/faceclustering/faceclusteringimpl.cpp',
      '<(FACE_ROOT)/faceclustering/faceclusters.cpp',
      '<(FACE_ROOT)/faceclustering/faceclusters.h',
      '<(FACE_ROOT)/facedetection/facedetector.h',
      '<(FACE_ROOT)/facedetection/facedetectorimpl.h',
      '<(FACE_ROOT)/facedetection/facedetectorimpl.cpp',
      '<(FACE_ROOT)/facefeature/elasticmatch.cpp',
      '<(FACE_ROOT)/facefeature/facefeature.h',
      '<(FACE_ROOT)/facefeature/facefeatureimpl.h',
      '<(FACE_ROOT)/facefeature/facefeatureimpl.cpp',
      '<(FACE_ROOT)/facefeature/facelandmark.h',
      '<(FACE_ROOT)/facefeature/HOG.cpp',
      '<(FACE_ROOT)/facefeature/LBP.cpp',
      '<(FACE_ROOT)/facerecognize/faceclassifier.h',
      '<(FACE_ROOT)/facerecognize/facerecognize.cpp',
      '<(FACE_ROOT)/facerecognize/intkey.cpp',
      '<(FACE_ROOT)/facerecognize/intkey.h',
      '<(FACE_ROOT)/include/facerecognize.h',
      '<(FACE_ROOT)/include/faceutils.h',
      '<(FACE_ROOT)/include/public.h',
      '<(FACE_CLUSTER)/action_cluster.h',
      '<(FACE_CLUSTER)/action_cluster.cc',
      '<(FACE_CLUSTER)/memcache.h',
      '<(FACE_CLUSTER)/memcache.cpp',
      '<(FACE_CLUSTER)/registry.cc',
      '../arch_diff/IdCacheReaderAdapter.h',
      '../arch_diff/IdCacheReaderAdapter.cpp',
      '../arch_diff/BuddyByIdReplicaAdapter.h',
      '../arch_diff/BuddyByIdReplicaAdapter.cpp',
      '../arch_diff/BuddyCheckHelper.h',
      '../arch_diff/IpAddr.hpp',
      '../arch_diff/Markable.hpp',
      '../arch_diff/Date.h',
      '../arch_diff/Channel.h',
      '../arch_diff/Channel.cpp',
      '../arch_diff/TaskManager.h',
      '../arch_diff/TaskManager.cpp',
      '../arch_diff/ThreadPoolExecutor.cpp',
      '../arch_diff/ThreadPoolScheduler.cpp',
      '../arch_diff/ClientInterface.h',
      '../arch_diff/ClusterClient.h',
      '../arch_diff/ClusterStateSubscriber.h',
      '../arch_diff/ClusterStateSubscriber.cpp',
      '../arch_diff/Singleton.h',
      '../arch_diff/SbjTopicI.h',
      '../arch_diff/SbjTopicI.cpp',
      '../arch_diff/AdapterI.cpp',
      '../arch_diff/AdapterI.h',
      '../arch_diff/site_xiaonei.h',
      '../arch_diff/site_xiaonei.cc',
    ],
   },

{ 'target_name': 'facestore.fcgi',
   'type': 'executable',
   'include_dirs':[
     '../cwf/src',
#    '/root/tair_bin/include',
#    '/usr/local/include/tbnet',
#    '/usr/local/include/tbsys',
   ],
   'dependencies':[
      '../cwf/gyp/base3.gyp:base3',
      'jsoncpp.gyp:json',
      '../cwf/gyp/cwf.gyp:cwf',
 '../cwf/gyp/cwf.gyp:cwfmain',
           'ice.gyp:utiladapter',
      'ice.gyp:oceadapter',
   ],
  'export_dependent_settings': ['jsoncpp.gyp:json'],
   'conditions':[
      ['OS=="linux"', {
        'libraries': ['-lboost_system',
                      '-lboost_thread',
                      '-lssl' , '-lmemcached', 
#                      '-ltairclientapi','-ltbsys','-ltbnet',
#                      '-L/root/tair_bin/lib/',
                      ],

        'link_settings': {
          'ldflags': [
           '-Wl,-rpath /usr/local/lib',
          ],
        },
     }],
   ],
   'sources': [
     '<(FACE_STORE)/action_face_store.cc',
     '<(FACE_STORE)/action_face_store.h',
      '<(FACE_STORE)/memcache.cpp',
      '<(FACE_STORE)/memcache.h',
     '<(FACE_STORE)/registry.cc',

    ],
   },


  ]
}

