import streamlit as st
import re

def check_password_strength(password):
    """
    Check password strength and provide specific feedback
    """
    score = 0
    improvements = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        improvements.append("Make your password at least 8 characters long")
    
    # Check uppercase and lowercase
    if not re.search(r'[A-Z]', password):
        improvements.append("Add uppercase letters (A-Z)")
    if not re.search(r'[a-z]', password):
        improvements.append("Add lowercase letters (a-z)")
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    
    # Check numbers
    if re.search(r'\d', password):
        score += 1
    else:
        improvements.append("Include at least one number (0-9)")
    
    # Check special characters
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        improvements.append("Add special characters (!@#$%^&*)")
    
    # Extra point for meeting all criteria
    if len(improvements) == 0:
        score += 1
    
    return score, improvements

# Set up the Streamlit page
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

# Add title and description
st.title("🔒 Password Strength Checker")
st.markdown("""
Enter your password below to check its strength. A strong password should have:
- At least 8 characters
- Mix of uppercase and lowercase letters
- At least one number
- At least one special character (!@#$%^&*)
""")

# Password input
password = st.text_input("Enter your password", type="password")

if password:
    score, improvements = check_password_strength(password)
    
    # Display strength based on score
    if score <= 2:
        st.error("### ❌ Weak Password")
        
        # Show specific improvements needed
        st.markdown("### 💡 To make your password stronger:")
        for improvement in improvements:
            st.warning(f"- {improvement}")
            
    elif score <= 4:
        st.warning("### ⚠️ Moderate Password")
        if improvements:
            st.markdown("### 💡 To make your password stronger:")
            for improvement in improvements:
                st.info(f"- {improvement}")
                
    else:
        # Success message for strong passwords
        st.success("""
        ### 🎉 Strong Password!
        
        Excellent! Your password meets all security criteria:
        - ✅ Good length
        - ✅ Mix of uppercase and lowercase letters
        - ✅ Contains numbers
        - ✅ Includes special characters
        
        Remember to use unique passwords for different accounts!
        """)
    
    # Show strength meter
    st.progress(score/5)
    
else:
    st.info("👆 Enter a password above to check its strength")

# Security note
st.markdown("---")
st.info("""
**Note:** This tool is for educational purposes only. 
Your password is never stored or transmitted anywhere.

**Tips for password security:**
- Use different passwords for different accounts
- Consider using a password manager
- Enable two-factor authentication when available
""")
