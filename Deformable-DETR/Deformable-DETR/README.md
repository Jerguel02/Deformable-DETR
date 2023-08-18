[**Deformable-DETR**](http://arxiv.org/abs/2010.04159): Deformable Transformers for End-to-End Object Detection


# Training

py main.py --output_dir my_output --coco_path ../dataset/ --lr 0.0002 --lr_backbone 0.00001 --batch_size 32 --enc_layers 6 --dec_layers 6 --no_aux_loss --amp

