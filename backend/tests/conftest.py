import warnings

# Suppress specific deprecation warnings
warnings.filterwarnings(
    "ignore", category=DeprecationWarning, message="Type google._upb._message.*"
)

# Suppress specific future warnings
warnings.filterwarnings(
    "ignore",
    category=FutureWarning,
    message="`clean_up_tokenization_spaces` was not set.*",
)
