#!/usr/bin/env python3
"""
VEO 3 Error Handling Demonstration
Shows the difference between naive and robust error handling approaches
"""

import requests
import json
from veo3_robust_client import VEO3RobustClient, VEO3ValidationError, VEO3APIError

# API Configuration
API_KEY = "20108f4bba626227a1bb5e281d1e5a64"
BASE_URL = "https://api.kie.ai/api/v1/veo"
HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def naive_approach(prompt, model="veo3_fast", aspect_ratio="16:9"):
    """
    Naive approach - direct API call without proper error handling
    This is how most implementations currently work
    """
    print(f"\n🔴 NAIVE APPROACH: Generating with prompt: '{prompt[:50]}...'")

    request_data = {
        "prompt": prompt,
        "model": model,
        "aspectRatio": aspect_ratio,
        "enableFallback": True
    }

    try:
        response = requests.post(
            f"{BASE_URL}/generate",
            headers=HEADERS,
            json=request_data,
            timeout=30
        )

        print(f"   HTTP Status: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            print(f"   ✅ Success! Response: {json.dumps(result, indent=2)}")
            return True
        else:
            print(f"   ❌ Failed! HTTP Error: {response.status_code}")
            return False

    except Exception as e:
        print(f"   ❌ Exception: {e}")
        return False

def robust_approach(prompt, model="veo3_fast", aspect_ratio="16:9"):
    """
    Robust approach using VEO3RobustClient with proper error handling
    """
    print(f"\n🟢 ROBUST APPROACH: Generating with prompt: '{prompt[:50]}...'")

    client = VEO3RobustClient()

    try:
        result = client.generate_video(
            prompt=prompt,
            model=model,
            aspect_ratio=aspect_ratio
        )

        print(f"   ✅ Success! Task ID: {result['task_id']}")
        print(f"   Message: {result['message']}")
        return True

    except VEO3ValidationError as e:
        print(f"   ⚠️  Validation Error: {e}")
        print(f"   → Fix your parameters and try again")
        return False

    except VEO3APIError as e:
        print(f"   ❌ API Error: {e}")
        print(f"   → Check API status or retry later")
        return False

    except Exception as e:
        print(f"   ❌ Unexpected Error: {e}")
        return False

def demonstrate_error_handling():
    """
    Demonstrate different error scenarios with both approaches
    """
    print("🧪 VEO 3 Error Handling Demonstration")
    print("=" * 60)
    print("Comparing naive vs robust error handling approaches")
    print("=" * 60)

    test_cases = [
        {
            "name": "Valid Request",
            "prompt": "A cinematic shot of a sunset over mountains",
            "model": "veo3_fast",
            "aspect_ratio": "16:9",
            "expected": "Should succeed"
        },
        {
            "name": "Empty Prompt",
            "prompt": "",
            "model": "veo3_fast",
            "aspect_ratio": "16:9",
            "expected": "Should fail with validation error"
        },
        {
            "name": "Invalid Model",
            "prompt": "A simple test video",
            "model": "invalid_model",
            "aspect_ratio": "16:9",
            "expected": "Should fail with validation error"
        },
        {
            "name": "Invalid Aspect Ratio",
            "prompt": "A simple test video",
            "model": "veo3_fast",
            "aspect_ratio": "4:3",
            "expected": "Should fail with validation error"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"TEST {i}: {test_case['name']}")
        print(f"Expected: {test_case['expected']}")
        print(f"{'='*60}")

        # Test naive approach
        naive_success = naive_approach(
            test_case['prompt'],
            test_case['model'],
            test_case['aspect_ratio']
        )

        # Test robust approach
        robust_success = robust_approach(
            test_case['prompt'],
            test_case['model'],
            test_case['aspect_ratio']
        )

        # Analysis
        print(f"\n📊 ANALYSIS:")
        if test_case['name'] == "Valid Request":
            if naive_success and robust_success:
                print(f"   ✅ Both approaches handled valid request correctly")
            else:
                print(f"   ❌ Valid request failed unexpectedly")
        else:
            print(f"   Naive approach: {'Failed ❌' if not naive_success else 'Succeeded ✅'}")
            print(f"   Robust approach: {'Failed ❌' if not robust_success else 'Succeeded ✅'}")

            if not naive_success and not robust_success:
                print(f"   ✅ Both approaches correctly rejected invalid input")
                print(f"   🎯 Robust approach provides better error messages")
            elif naive_success and not robust_success:
                print(f"   ⚠️  Naive approach wasted API call on invalid input")
                print(f"   ✅ Robust approach prevented wasted API call")
            else:
                print(f"   ❓ Unexpected result pattern")

    print(f"\n{'='*60}")
    print("🎯 KEY TAKEAWAYS")
    print(f"{'='*60}")
    print("1. VEO 3 API returns HTTP 200 for ALL requests (even errors)")
    print("2. Actual error codes are embedded in JSON response body")
    print("3. Naive approach misses validation errors → wasted API calls")
    print("4. Robust approach prevents invalid requests → cost savings")
    print("5. Proper error messages improve user experience")
    print("6. Pre-validation catches errors before making expensive API calls")

    print(f"\n💡 RECOMMENDATIONS:")
    print("• Use VEO3RobustClient for all VEO 3 API interactions")
    print("• Implement client-side validation to prevent wasted API calls")
    print("• Parse JSON response body for actual error codes")
    print("• Provide clear error messages to users")
    print("• Add retry logic for transient failures")

if __name__ == "__main__":
    demonstrate_error_handling()