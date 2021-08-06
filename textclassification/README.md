# Text Classification

## gpu 존재 시

- python train.py --model_fn ./models/review.pth --train_fn ../review.sorted.uniq.refined.tok.shuf.train.tsv --gpu_id 0 --batch_size 128 --n_epochs 10 --word_vec_size 256 --dropout .3 --rnn --hidden_size 512 --n_layers 4 --cnn --window_sizes 3 4 5 6 7 8 --n_filters 128 128 128 128 128 128

## 미 존재 시

- python train.py --model_fn ./models/review.pth --train_fn ../review.sorted.uniq.refined.tok.shuf.train.tsv --batch_size 128 --n_epochs 10 --word_vec_size 256 --dropout .3 --rnn --hidden_size 512 --n_layers 4 --cnn --window_sizes 3 4 5 6 7 8 --n_filters 128 128 128 128 128 128
