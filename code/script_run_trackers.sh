#!/bin/sh

##############################################################################################
############################### Tracker CSRT (OpenCV_contrib) ################################
##############################################################################################
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/CSRT/01/01-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/CSRT/02/02-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/CSRT/03/03-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/CSRT/04/04-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/CSRT/05/05-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/CSRT/06/06-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/CSRT/07/07-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/CSRT/08/08-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/CSRT/09/09-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/CSRT/10/10-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/CSRT/11/11-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/CSRT/12/12-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/CSRT/13/13-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/CSRT/14/14-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/CSRT/15/15-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/CSRT/16/16-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/CSRT/17/17-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/CSRT/18/18-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/CSRT/19/19-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/CSRT/20/20-result-default.txt
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/CSRT/21/21-result-default.txt

# python run_opencv_tracking.py -t CSRT -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/CSRT/01/01-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/CSRT/02/02-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/CSRT/03/03-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/CSRT/04/04-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/CSRT/05/05-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/CSRT/06/06-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/CSRT/07/07-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/CSRT/08/08-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/CSRT/09/09-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/CSRT/10/10-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/CSRT/11/11-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/CSRT/12/12-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/CSRT/13/13-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/CSRT/14/14-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/CSRT/15/15-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/CSRT/16/16-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/CSRT/17/17-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/CSRT/18/18-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/CSRT/19/19-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/CSRT/20/20-result-border.txt -border
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/CSRT/21/21-result-border.txt -border

# python run_opencv_tracking.py -t CSRT -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/CSRT/01/01-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/CSRT/02/02-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/CSRT/03/03-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/CSRT/04/04-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/CSRT/05/05-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/CSRT/06/06-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/CSRT/07/07-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/CSRT/08/08-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/CSRT/09/09-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/CSRT/10/10-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/CSRT/11/11-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/CSRT/12/12-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/CSRT/13/13-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/CSRT/14/14-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/CSRT/15/15-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/CSRT/16/16-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/CSRT/17/17-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/CSRT/18/18-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/CSRT/19/19-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/CSRT/20/20-result-nfov.txt -nfov
# python run_opencv_tracking.py -t CSRT -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/CSRT/21/21-result-nfov.txt -nfov


##############################################################################################
########################### Tracker MEDIANFLOW (OpenCV_contrib) ##############################
##############################################################################################
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/MEDIANFLOW/01/01-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/MEDIANFLOW/02/02-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/MEDIANFLOW/03/03-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/MEDIANFLOW/04/04-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/MEDIANFLOW/05/05-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/MEDIANFLOW/06/06-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/MEDIANFLOW/07/07-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/MEDIANFLOW/08/08-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/MEDIANFLOW/09/09-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/MEDIANFLOW/10/10-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/MEDIANFLOW/11/11-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/MEDIANFLOW/12/12-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/MEDIANFLOW/13/13-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/MEDIANFLOW/14/14-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/MEDIANFLOW/15/15-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/MEDIANFLOW/16/16-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/MEDIANFLOW/17/17-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/MEDIANFLOW/18/18-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/MEDIANFLOW/19/19-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/MEDIANFLOW/20/20-result-default.txt
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/MEDIANFLOW/21/21-result-default.txt

# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/MEDIANFLOW/01/01-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/MEDIANFLOW/02/02-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/MEDIANFLOW/03/03-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/MEDIANFLOW/04/04-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/MEDIANFLOW/05/05-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/MEDIANFLOW/06/06-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/MEDIANFLOW/07/07-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/MEDIANFLOW/08/08-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/MEDIANFLOW/09/09-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/MEDIANFLOW/10/10-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/MEDIANFLOW/11/11-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/MEDIANFLOW/12/12-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/MEDIANFLOW/13/13-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/MEDIANFLOW/14/14-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/MEDIANFLOW/15/15-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/MEDIANFLOW/16/16-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/MEDIANFLOW/17/17-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/MEDIANFLOW/18/18-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/MEDIANFLOW/19/19-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/MEDIANFLOW/20/20-result-border.txt -border
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/MEDIANFLOW/21/21-result-border.txt -border

# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/MEDIANFLOW/01/01-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/MEDIANFLOW/02/02-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/MEDIANFLOW/03/03-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/MEDIANFLOW/04/04-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/MEDIANFLOW/05/05-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/MEDIANFLOW/06/06-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/MEDIANFLOW/07/07-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/MEDIANFLOW/08/08-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/MEDIANFLOW/09/09-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/MEDIANFLOW/10/10-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/MEDIANFLOW/11/11-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/MEDIANFLOW/12/12-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/MEDIANFLOW/13/13-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/MEDIANFLOW/14/14-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/MEDIANFLOW/15/15-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/MEDIANFLOW/16/16-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/MEDIANFLOW/17/17-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/MEDIANFLOW/18/18-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/MEDIANFLOW/19/19-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/MEDIANFLOW/20/20-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MEDIANFLOW -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/MEDIANFLOW/21/21-result-nfov.txt -nfov


##############################################################################################
############################### Tracker KCF (OpenCV_contrib) ################################
##############################################################################################
# python run_opencv_tracking.py -t KCF -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/KCF/01/01-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/KCF/02/02-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/KCF/03/03-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/KCF/04/04-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/KCF/05/05-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/KCF/06/06-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/KCF/07/07-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/KCF/08/08-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/KCF/09/09-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/KCF/10/10-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/KCF/11/11-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/KCF/12/12-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/KCF/13/13-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/KCF/14/14-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/KCF/15/15-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/KCF/16/16-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/KCF/17/17-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/KCF/18/18-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/KCF/19/19-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/KCF/20/20-result-default.txt
# python run_opencv_tracking.py -t KCF -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/KCF/21/21-result-default.txt

# python run_opencv_tracking.py -t KCF -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/KCF/01/01-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/KCF/02/02-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/KCF/03/03-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/KCF/04/04-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/KCF/05/05-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/KCF/06/06-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/KCF/07/07-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/KCF/08/08-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/KCF/09/09-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/KCF/10/10-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/KCF/11/11-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/KCF/12/12-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/KCF/13/13-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/KCF/14/14-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/KCF/15/15-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/KCF/16/16-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/KCF/17/17-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/KCF/18/18-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/KCF/19/19-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/KCF/20/20-result-border.txt -border
# python run_opencv_tracking.py -t KCF -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/KCF/21/21-result-border.txt -border

# python run_opencv_tracking.py -t KCF -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/KCF/01/01-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/KCF/02/02-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/KCF/03/03-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/KCF/04/04-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/KCF/05/05-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/KCF/06/06-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/KCF/07/07-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/KCF/08/08-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/KCF/09/09-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/KCF/10/10-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/KCF/11/11-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/KCF/12/12-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/KCF/13/13-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/KCF/14/14-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/KCF/15/15-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/KCF/16/16-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/KCF/17/17-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/KCF/18/18-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/KCF/19/19-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/KCF/20/20-result-nfov.txt -nfov
# python run_opencv_tracking.py -t KCF -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/KCF/21/21-result-nfov.txt -nfov


##############################################################################################
############################### Tracker MIL (OpenCV_contrib) ################################
##############################################################################################
# python run_opencv_tracking.py -t MIL -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/MIL/01/01-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/MIL/02/02-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/MIL/03/03-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/MIL/04/04-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/MIL/05/05-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/MIL/06/06-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/MIL/07/07-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/MIL/08/08-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/MIL/09/09-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/MIL/10/10-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/MIL/11/11-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/MIL/12/12-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/MIL/13/13-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/MIL/14/14-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/MIL/15/15-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/MIL/16/16-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/MIL/17/17-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/MIL/18/18-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/MIL/19/19-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/MIL/20/20-result-default.txt
# python run_opencv_tracking.py -t MIL -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/MIL/21/21-result-default.txt

# python run_opencv_tracking.py -t MIL -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/MIL/01/01-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/MIL/02/02-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/MIL/03/03-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/MIL/04/04-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/MIL/05/05-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/MIL/06/06-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/MIL/07/07-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/MIL/08/08-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/MIL/09/09-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/MIL/10/10-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/MIL/11/11-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/MIL/12/12-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/MIL/13/13-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/MIL/14/14-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/MIL/15/15-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/MIL/16/16-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/MIL/17/17-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/MIL/18/18-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/MIL/19/19-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/MIL/20/20-result-border.txt -border
# python run_opencv_tracking.py -t MIL -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/MIL/21/21-result-border.txt -border

# python run_opencv_tracking.py -t MIL -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/MIL/01/01-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/MIL/02/02-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/MIL/03/03-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/MIL/04/04-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/MIL/05/05-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/MIL/06/06-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/MIL/07/07-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/MIL/08/08-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/MIL/09/09-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/MIL/10/10-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/MIL/11/11-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/MIL/12/12-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/MIL/13/13-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/MIL/14/14-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/MIL/15/15-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/MIL/16/16-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/MIL/17/17-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/MIL/18/18-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/MIL/19/19-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/MIL/20/20-result-nfov.txt -nfov
# python run_opencv_tracking.py -t MIL -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/MIL/21/21-result-nfov.txt -nfov


##############################################################################################
############################### Tracker TLD (OpenCV_contrib) ################################
##############################################################################################
# python run_opencv_tracking.py -t TLD -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/TLD/01/01-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/TLD/02/02-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/TLD/03/03-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/TLD/04/04-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/TLD/05/05-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/TLD/06/06-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/TLD/07/07-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/TLD/08/08-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/TLD/09/09-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/TLD/10/10-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/TLD/11/11-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/TLD/12/12-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/TLD/13/13-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/TLD/14/14-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/TLD/15/15-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/TLD/16/16-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/TLD/17/17-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/TLD/18/18-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/TLD/19/19-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/TLD/20/20-result-default.txt
# python run_opencv_tracking.py -t TLD -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/TLD/21/21-result-default.txt

# python run_opencv_tracking.py -t TLD -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/TLD/01/01-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/TLD/02/02-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/TLD/03/03-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/TLD/04/04-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/TLD/05/05-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/TLD/06/06-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/TLD/07/07-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/TLD/08/08-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/TLD/09/09-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/TLD/10/10-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/TLD/11/11-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/TLD/12/12-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/TLD/13/13-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/TLD/14/14-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/TLD/15/15-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/TLD/16/16-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/TLD/17/17-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/TLD/18/18-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/TLD/19/19-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/TLD/20/20-result-border.txt -border
# python run_opencv_tracking.py -t TLD -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/TLD/21/21-result-border.txt -border

# python run_opencv_tracking.py -t TLD -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/TLD/01/01-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/TLD/02/02-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/TLD/03/03-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/TLD/04/04-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/TLD/05/05-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/TLD/06/06-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/TLD/07/07-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/TLD/08/08-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/TLD/09/09-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/TLD/10/10-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/TLD/11/11-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/TLD/12/12-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/TLD/13/13-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/TLD/14/14-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/TLD/15/15-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/TLD/16/16-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/TLD/17/17-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/TLD/18/18-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/TLD/19/19-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/TLD/20/20-result-nfov.txt -nfov
# python run_opencv_tracking.py -t TLD -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/TLD/21/21-result-nfov.txt -nfov



##############################################################################################
############################### Tracker ECO (pytracking) #####################################
##############################################################################################
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/ECO/01/01-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/ECO/02/02-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/ECO/03/03-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/ECO/04/04-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/ECO/05/05-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/ECO/06/06-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/ECO/07/07-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/ECO/08/08-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/ECO/09/09-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/ECO/10/10-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/ECO/11/11-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/ECO/12/12-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/ECO/13/13-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/ECO/14/14-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/ECO/15/15-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/ECO/16/16-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/ECO/17/17-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/ECO/18/18-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/ECO/19/19-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/ECO/20/20-result-default.txt
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/ECO/21/21-result-default.txt

# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/ECO/01/01-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/ECO/02/02-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/ECO/03/03-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/ECO/04/04-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/ECO/05/05-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/ECO/06/06-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/ECO/07/07-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/ECO/08/08-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/ECO/09/09-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/ECO/10/10-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/ECO/11/11-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/ECO/12/12-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/ECO/13/13-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/ECO/14/14-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/ECO/15/15-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/ECO/16/16-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/ECO/17/17-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/ECO/18/18-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/ECO/19/19-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/ECO/20/20-result-border.txt -border
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/ECO/21/21-result-border.txt -border

# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/ECO/01/01-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/ECO/02/02-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/ECO/03/03-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/ECO/04/04-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/ECO/05/05-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/ECO/06/06-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/ECO/07/07-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/ECO/08/08-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/ECO/09/09-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/ECO/10/10-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/ECO/11/11-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/ECO/12/12-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/ECO/13/13-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/ECO/14/14-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/ECO/15/15-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/ECO/16/16-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/ECO/17/17-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/ECO/18/18-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/ECO/19/19-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/ECO/20/20-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py eco default annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/ECO/21/21-result-nfov.txt -nfov


##############################################################################################
############################### Tracker ATOM (pytracking) ####################################
##############################################################################################
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/ATOM/01/01-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/ATOM/02/02-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/ATOM/03/03-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/ATOM/04/04-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/ATOM/05/05-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/ATOM/06/06-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/ATOM/07/07-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/ATOM/08/08-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/ATOM/09/09-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/ATOM/10/10-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/ATOM/11/11-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/ATOM/12/12-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/ATOM/13/13-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/ATOM/14/14-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/ATOM/15/15-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/ATOM/16/16-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/ATOM/17/17-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/ATOM/18/18-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/ATOM/19/19-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/ATOM/20/20-result-default.txt
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/ATOM/21/21-result-default.txt

# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/ATOM/01/01-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/ATOM/02/02-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/ATOM/03/03-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/ATOM/04/04-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/ATOM/05/05-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/ATOM/06/06-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/ATOM/07/07-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/ATOM/08/08-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/ATOM/09/09-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/ATOM/10/10-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/ATOM/11/11-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/ATOM/12/12-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/ATOM/13/13-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/ATOM/14/14-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/ATOM/15/15-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/ATOM/16/16-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/ATOM/17/17-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/ATOM/18/18-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/ATOM/19/19-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/ATOM/20/20-result-border.txt -border
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/ATOM/21/21-result-border.txt -border

# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/ATOM/01/01-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/ATOM/02/02-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/ATOM/03/03-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/ATOM/04/04-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/ATOM/05/05-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/ATOM/06/06-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/ATOM/07/07-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/ATOM/08/08-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/ATOM/09/09-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/ATOM/10/10-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/ATOM/11/11-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/ATOM/12/12-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/ATOM/13/13-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/ATOM/14/14-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/ATOM/15/15-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/ATOM/16/16-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/ATOM/17/17-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/ATOM/18/18-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/ATOM/19/19-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/ATOM/20/20-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py atom default annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/ATOM/21/21-result-nfov.txt -nfov



##############################################################################################
############################### Tracker DiMP (pytracking) ####################################
##############################################################################################
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/DiMP/01/01-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/DiMP/02/02-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/DiMP/03/03-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/DiMP/04/04-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/DiMP/05/05-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/DiMP/06/06-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/DiMP/07/07-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/DiMP/08/08-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/DiMP/09/09-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/DiMP/10/10-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/DiMP/11/11-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/DiMP/12/12-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/DiMP/13/13-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/DiMP/14/14-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/DiMP/15/15-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/DiMP/16/16-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/DiMP/17/17-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/DiMP/18/18-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/DiMP/19/19-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/DiMP/20/20-result-default.txt
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/DiMP/21/21-result-default.txt

# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/DiMP/01/01-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/DiMP/02/02-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/DiMP/03/03-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/DiMP/04/04-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/DiMP/05/05-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/DiMP/06/06-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/DiMP/07/07-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/DiMP/08/08-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/DiMP/09/09-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/DiMP/10/10-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/DiMP/11/11-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/DiMP/12/12-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/DiMP/13/13-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/DiMP/14/14-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/DiMP/15/15-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/DiMP/16/16-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/DiMP/17/17-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/DiMP/18/18-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/DiMP/19/19-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/DiMP/20/20-result-border.txt -border
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/DiMP/21/21-result-border.txt -border

# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/DiMP/01/01-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/DiMP/02/02-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/DiMP/03/03-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/DiMP/04/04-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/DiMP/05/05-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/DiMP/06/06-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/DiMP/07/07-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/DiMP/08/08-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/DiMP/09/09-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/DiMP/10/10-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/DiMP/11/11-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/DiMP/12/12-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/DiMP/13/13-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/DiMP/14/14-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/DiMP/15/15-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/DiMP/16/16-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/DiMP/17/17-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/DiMP/18/18-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/DiMP/19/19-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/DiMP/20/20-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py dimp dimp50 annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/DiMP/21/21-result-nfov.txt -nfov



##############################################################################################
############################### Tracker KYS (pytracking) #####################################
##############################################################################################
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/KYS/01/01-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/KYS/02/02-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/KYS/03/03-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/KYS/04/04-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/KYS/05/05-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/KYS/06/06-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/KYS/07/07-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/KYS/08/08-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/KYS/09/09-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/KYS/10/10-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/KYS/11/11-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/KYS/12/12-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/KYS/13/13-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/KYS/14/14-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/KYS/15/15-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/KYS/16/16-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/KYS/17/17-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/KYS/18/18-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/KYS/19/19-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/KYS/20/20-result-default.txt
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/KYS/21/21-result-default.txt

# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/KYS/01/01-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/KYS/02/02-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/KYS/03/03-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/KYS/04/04-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/KYS/05/05-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/KYS/06/06-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/KYS/07/07-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/KYS/08/08-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/KYS/09/09-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/KYS/10/10-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/KYS/11/11-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/KYS/12/12-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/KYS/13/13-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/KYS/14/14-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/KYS/15/15-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/KYS/16/16-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/KYS/17/17-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/KYS/18/18-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/KYS/19/19-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/KYS/20/20-result-border.txt -border
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/KYS/21/21-result-border.txt -border

# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/KYS/01/01-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/KYS/02/02-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/KYS/03/03-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/KYS/04/04-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/KYS/05/05-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/KYS/06/06-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/KYS/07/07-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/KYS/08/08-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/KYS/09/09-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/KYS/10/10-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/KYS/11/11-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/KYS/12/12-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/KYS/13/13-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/KYS/14/14-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/KYS/15/15-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/KYS/16/16-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/KYS/17/17-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/KYS/18/18-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/KYS/19/19-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/KYS/20/20-result-nfov.txt -nfov
# python pytracking/pytracking/run_video_360.py kys default annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/KYS/21/21-result-nfov.txt -nfov



##############################################################################################
############################# Tracker DaSiamRPN (DaSiamRPN) ##################################
##############################################################################################
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/DaSiamRPN/01/01-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/DaSiamRPN/02/02-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/DaSiamRPN/03/03-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/DaSiamRPN/04/04-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/DaSiamRPN/05/05-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/DaSiamRPN/06/06-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/DaSiamRPN/07/07-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/DaSiamRPN/08/08-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/DaSiamRPN/09/09-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/DaSiamRPN/10/10-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/DaSiamRPN/11/11-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/DaSiamRPN/12/12-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/DaSiamRPN/13/13-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/DaSiamRPN/14/14-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/DaSiamRPN/15/15-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/DaSiamRPN/16/16-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/DaSiamRPN/17/17-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/DaSiamRPN/18/18-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/DaSiamRPN/19/19-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/DaSiamRPN/20/20-result-default.txt
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/DaSiamRPN/21/21-result-default.txt

# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/DaSiamRPN/01/01-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/DaSiamRPN/02/02-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/DaSiamRPN/03/03-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/DaSiamRPN/04/04-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/DaSiamRPN/05/05-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/DaSiamRPN/06/06-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/DaSiamRPN/07/07-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/DaSiamRPN/08/08-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/DaSiamRPN/09/09-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/DaSiamRPN/10/10-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/DaSiamRPN/11/11-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/DaSiamRPN/12/12-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/DaSiamRPN/13/13-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/DaSiamRPN/14/14-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/DaSiamRPN/15/15-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/DaSiamRPN/16/16-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/DaSiamRPN/17/17-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/DaSiamRPN/18/18-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/DaSiamRPN/19/19-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/DaSiamRPN/20/20-result-border.txt -border
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/DaSiamRPN/21/21-result-border.txt -border

# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/DaSiamRPN/01/01-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/DaSiamRPN/02/02-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/DaSiamRPN/03/03-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/DaSiamRPN/04/04-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/DaSiamRPN/05/05-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/DaSiamRPN/06/06-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/DaSiamRPN/07/07-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/DaSiamRPN/08/08-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/DaSiamRPN/09/09-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/DaSiamRPN/10/10-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/DaSiamRPN/11/11-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/DaSiamRPN/12/12-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/DaSiamRPN/13/13-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/DaSiamRPN/14/14-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/DaSiamRPN/15/15-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/DaSiamRPN/16/16-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/DaSiamRPN/17/17-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/DaSiamRPN/18/18-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/DaSiamRPN/19/19-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/DaSiamRPN/20/20-result-nfov.txt -nfov
# python DaSiamRPN/code/run_video_360.py -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/DaSiamRPN/21/21-result-nfov.txt -nfov


##############################################################################################
################################# Tracker Ocean (TracKit) ####################################
##############################################################################################
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/Ocean/01/01-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/Ocean/02/02-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/Ocean/03/03-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/Ocean/04/04-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/Ocean/05/05-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/Ocean/06/06-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/Ocean/07/07-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/Ocean/08/08-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/Ocean/09/09-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/Ocean/10/10-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/Ocean/11/11-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/Ocean/12/12-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/Ocean/13/13-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/Ocean/14/14-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/Ocean/15/15-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/Ocean/16/16-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/Ocean/17/17-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/Ocean/18/18-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/Ocean/19/19-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/Ocean/20/20-result-default.txt
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/Ocean/21/21-result-default.txt

# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/Ocean/01/01-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/Ocean/02/02-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/Ocean/03/03-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/Ocean/04/04-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/Ocean/05/05-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/Ocean/06/06-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/Ocean/07/07-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/Ocean/08/08-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/Ocean/09/09-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/Ocean/10/10-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/Ocean/11/11-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/Ocean/12/12-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/Ocean/13/13-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/Ocean/14/14-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/Ocean/15/15-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/Ocean/16/16-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/Ocean/17/17-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/Ocean/18/18-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/Ocean/19/19-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/Ocean/20/20-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/Ocean/21/21-result-border.txt -border

# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/Ocean/01/01-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/Ocean/02/02-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/Ocean/03/03-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/Ocean/04/04-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/Ocean/05/05-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/Ocean/06/06-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/Ocean/07/07-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/Ocean/08/08-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/Ocean/09/09-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/Ocean/10/10-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/Ocean/11/11-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/Ocean/12/12-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/Ocean/13/13-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/Ocean/14/14-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/Ocean/15/15-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/Ocean/16/16-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/Ocean/17/17-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/Ocean/18/18-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/Ocean/19/19-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/Ocean/20/20-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch Ocean --resume TracKit/snapshot/OceanV19on.pth -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/Ocean/21/21-result-nfov.txt -nfov



##############################################################################################
################################# Tracker SiamDW (TracKit) ###################################
##############################################################################################
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/SiamDW/01/01-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/SiamDW/02/02-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/SiamDW/03/03-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/SiamDW/04/04-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/SiamDW/05/05-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/SiamDW/06/06-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/SiamDW/07/07-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/SiamDW/08/08-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/SiamDW/09/09-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/SiamDW/10/10-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/SiamDW/11/11-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/SiamDW/12/12-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/SiamDW/13/13-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/SiamDW/14/14-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/SiamDW/15/15-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/SiamDW/16/16-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/SiamDW/17/17-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/SiamDW/18/18-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/SiamDW/19/19-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/SiamDW/20/20-result-default.txt
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/SiamDW/21/21-result-default.txt

# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/SiamDW/01/01-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/SiamDW/02/02-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/SiamDW/03/03-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/SiamDW/04/04-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/SiamDW/05/05-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/SiamDW/06/06-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/SiamDW/07/07-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/SiamDW/08/08-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/SiamDW/09/09-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/SiamDW/10/10-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/SiamDW/11/11-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/SiamDW/12/12-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/SiamDW/13/13-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/SiamDW/14/14-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/SiamDW/15/15-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/SiamDW/16/16-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/SiamDW/17/17-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/SiamDW/18/18-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/SiamDW/19/19-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/SiamDW/20/20-result-border.txt -border
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/SiamDW/21/21-result-border.txt -border

# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/01/01.mp4 -gt annotation/dataset/01/groundtruth.txt -r annotation/results/SiamDW/01/01-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/02/02.mp4 -gt annotation/dataset/02/groundtruth.txt -r annotation/results/SiamDW/02/02-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/03/03.mp4 -gt annotation/dataset/03/groundtruth.txt -r annotation/results/SiamDW/03/03-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/04/04.mp4 -gt annotation/dataset/04/groundtruth.txt -r annotation/results/SiamDW/04/04-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/05/05.mp4 -gt annotation/dataset/05/groundtruth.txt -r annotation/results/SiamDW/05/05-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/06/06.mp4 -gt annotation/dataset/06/groundtruth.txt -r annotation/results/SiamDW/06/06-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/07/07.mp4 -gt annotation/dataset/07/groundtruth.txt -r annotation/results/SiamDW/07/07-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/08/08.mp4 -gt annotation/dataset/08/groundtruth.txt -r annotation/results/SiamDW/08/08-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/09/09.mp4 -gt annotation/dataset/09/groundtruth.txt -r annotation/results/SiamDW/09/09-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/10/10.mp4 -gt annotation/dataset/10/groundtruth.txt -r annotation/results/SiamDW/10/10-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/11/11.mp4 -gt annotation/dataset/11/groundtruth.txt -r annotation/results/SiamDW/11/11-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/12/12.mp4 -gt annotation/dataset/12/groundtruth.txt -r annotation/results/SiamDW/12/12-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/13/13.mp4 -gt annotation/dataset/13/groundtruth.txt -r annotation/results/SiamDW/13/13-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/14/14.mp4 -gt annotation/dataset/14/groundtruth.txt -r annotation/results/SiamDW/14/14-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/15/15.mp4 -gt annotation/dataset/15/groundtruth.txt -r annotation/results/SiamDW/15/15-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/16/16.mp4 -gt annotation/dataset/16/groundtruth.txt -r annotation/results/SiamDW/16/16-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/17/17.mp4 -gt annotation/dataset/17/groundtruth.txt -r annotation/results/SiamDW/17/17-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/18/18.MP4 -gt annotation/dataset/18/groundtruth.txt -r annotation/results/SiamDW/18/18-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/19/19.MP4 -gt annotation/dataset/19/groundtruth.txt -r annotation/results/SiamDW/19/19-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/20/20.MP4 -gt annotation/dataset/20/groundtruth.txt -r annotation/results/SiamDW/20/20-result-nfov.txt -nfov
# python TracKit/tracking/run_video_360.py --arch SiamDW --resume TracKit/snapshot/siamdw_res22w.pth -v annotation/dataset/21/21.mp4 -gt annotation/dataset/21/groundtruth.txt -r annotation/results/SiamDW/21/21-result-nfov.txt -nfov

