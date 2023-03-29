import streamlit as st

st.title('Introduction')
topside1, topside2 = st.columns([3, 1])
topside1.markdown(
"""
Cervical-level spinal cord injury (SCI) negatively impacts upper extremity (UE) function to varying degrees and typically results in reduced independence or tetraplegia [1]. The Capabilities of Upper Extremity Test (CUE-T) was developed to capture UE function through different arm and hand tasks in individuals with tetraplegia and has been established as an accurate clinical assessment [2]. While clinical assessments capture cross-sectional information, there is a demand for technologies that can passively monitor UE function without the need for clinicians and researchers in the community. 

"""
)
topside2.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBp2hfuburBPCyBye60gzNdiLTEzwa0B5Iuw&usqp=CAU', use_column_width=True)
"""
Novelty detection is one such method that provides key ingredients to identify and monitor UE function over time, especially when paired with real-world monitoring devices such as wearable sensors. In general, novelty detection is a semi-supervised machine learning technique used to identify characteristics of data samples collected during a baseline assessment and then used on new data samples to recognize characteristics that appear different or new [3]. 

Novelty detection methods have been used in previous research with movement data, including wearable-sensor-captured movement data, to monitor clinically relevant outcomes, such as gait, falls, and abnormal movements [3-5]. To our knowledge, novelty detection methods have not been applied to movement data collected from individuals with SCI. Previous research in SCI has used multiple wearable sensors to detect and classify physical activities or quantify movement kinematics [6,7]. While these metrics are useful in understanding the magnitude and frequency of physical movement, they lack critical context regarding when and how function recovers over time. 

**Therefore, the overarching goal of this study is to assess the relationship between novel UE movement pattern scores identified through novelty detection methods and clinical UE function scores as measured by the CUE-T.** 
"""